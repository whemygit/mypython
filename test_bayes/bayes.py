#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

def LoadDataSet():
    '''数据加载函数，主要用于演示样例所用，说明建立模型所需要的基础数据格式
    输入：文本列表组成的列表，各文本所属类型的向量，两类别用0,1表示
    输出:同输入'''
    postingList=[['my','dog','has','flea',
                  'problems','help','please'],
                 ['maybe','not','take','him',
                  'to','dog','park','stupid'],
                 ['my','dalmation','is','so','cute',
                  'I','love','him'],
                 ['stop','posting','stupid','worthless','garbage'],
                 ['mr','licks','ate','my','steak','how','to','stop','him'],
                 ['quit','buying','worthless','dog','food','stupid']]
    classVec=[0,1,0,1,0,1]
    return postingList,classVec

def createVocabList(dataSet):
    '''词库创建函数，用于利用输入的文本生成词库集，原则上包含所有在所有的文本中出现过的词（每个词出现一次的词集）
                   ，但实际处理工程中可添加去停用词等预处理
    输入：待训练的所有文本列表组成的列表，及LoadDataSet()输出的第一个参数
    输出：组成文本的所有词的词集，所有词组成的列表'''
    vocabSet=set([])
    for document in dataSet:
        vocabSet=vocabSet | set(document)
    return list(vocabSet)

def setOfWords2Vec(vocabList,inputSet):
    '''向量转换函数：将某一文本词列表转换为与词库长度相同，各元素用0或1表示的词向量，0表示在待转换的
                    文本中没有出现词库对应位置的词，1表示出现了词库对用位置的词
    输入：词库，待转换的文本词列表
    输出：转换后的0,1组成的词向量'''
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
        else:print "the word: %s is not in my Vocabulary!" %word
    return returnVec

def bagOfWords2Vec(vocabList,inputSet):
    '''向量转换函数：输入与seyOfWords2Vec完全相同，只不过在输出上有所变化，前者输出0和1组成的向量，0
    表示不出现，1表示出现，并没有出现次数的特征。而本函数为了体现每个词出现次数的特征，会输出对应词
    出现次数，一遇到出现该词，则在原来的基础上+1'''
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]+=1
        else:print "the word: %s is not in my Vocabulary!" %word
    return returnVec


from numpy import *
def trainNBO(trainMatrix,trainCategory):
    '''训练算法函数：利用由上一步转换成的各文本词向量组成的词向量列表（该列表长度为文档个数，每个元素
                    的长度为词库长度的0,1词向量），以及各文本所属类型的向量，计算词库中各词属于指定文本
                    类别的条件概率向量和所有文档中类别1的文档出现的概率
    输入：词向量列表，文本所属类型向量
    输出：每个类别情况下词库中每个词出现的条件概率向量（某词出现次数/本类别文本出现的所有词个数），类别1文档出现的概率
    tips：为了考虑全面，假设所有的词至少出现一次，哪怕是在所有的文本中从没出现过的词，因此初始值p0Num
     和平Num均由zeros(numWords)，改为ones(numWords)，总概率等于1（出现和不出现），分母p0Denom和p1Denom
     初始值设为2.0
     防止小数乘小数结果太小，则提前对概率值取对数'''
    numTrainDocs=len(trainMatrix)
    numWords=len(trainMatrix[0])
    pAbusive=sum(trainCategory)/float(numTrainDocs)
    p0Num=ones(numWords);p1Num=ones(numWords)
    p0Denom=2.0;p1Denom=2.0
    for i in range(numTrainDocs):
        if trainCategory[i]==1:
            p1Num+=trainMatrix[i]
            p1Denom+=sum(trainMatrix[i])
        else:
            p0Num+=trainMatrix[i]
            p0Denom+=sum(trainMatrix[i])
    p1Vect=log(p1Num/p1Denom)
    p0Vect=log(p0Num/p0Denom)
    return p0Vect,p1Vect,pAbusive

#以下注释代码用于测试
# listOPosts,listClasses=LoadDataSet()
# print listOPosts
# myVocabList=createVocabList(listOPosts)
# print myVocabList
#
#
# trainMat=[]
# for  postinDoc in listOPosts:
#     trainMat.append(setOfWords2Vec(myVocabList,postinDoc))
# print trainMat
#
# p0V,p1V,pAb=trainNBO(trainMat,listClasses)
# print p0V,p1V,pAb

def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    '''分类函数：计算后验概率，根据概率比较，判断待分类文本应属于概率较大的类
    输入：待分类的文本词向量，训练函数输出的结果
    输出：待分类文本所属类别（1或0）'''
    p1=sum(vec2Classify*p1Vec)+log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + log(1-pClass1)
    if p1>p0:
        return 1
    else:
        return 0

def testingNB():
    '''测试函数'''
    listOPosts,listClasses=LoadDataSet()
    myVocabList=createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(bagOfWords2Vec(myVocabList,postinDoc))
        p0V,p1V,pAb=trainNBO(array(trainMat),array(listClasses))
    testEntry=['love','my','dalmation']
    thisDoc=array(bagOfWords2Vec(myVocabList,testEntry))
    print testEntry,'classified as :',classifyNB(thisDoc,p0V,p1V,pAb)

testingNB()

def textParse(bigString):
    import re
    listOfTokens=re.split(r'w*',bigString)
    return [tok.lower() for tok in listOfTokens if len(tok)>2]

def spamTest():
    docList=[];classList=[];fullText=[]
    for i in range(1,26):                          #读取样本
        wordList=textParse(open('aa%d'%i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open('aa%d'%i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList=createVocabList(docList)              #生成词库
    trainingSet=range(50);testSet=[]                #训练集和测试集序号
    for i in range(10):
        randIndex=int(random.uniform(0,len(trainingSet)))     #随机序列号
        testSet.append(trainingSet[randIndex])                #随机序列加入测试集
        del(trainingSet[randIndex])                           #同时将测试集中对应序列号删除
    trainMat=[];trainClasses=[]
    for docIndex in trainingSet:                              #根据对应序列生成训练集及类别向量
        trainMat.append(bagOfWords2Vec(vocabList,docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam=trainNBO(trainMat,trainClasses)              #训练模型
    errorCount=0
    for docIndex in testSet:                                   #逐条测试测试集，测试结果与实际不符中错误数+1
        wordVector=bagOfWords2Vec(vocabList,docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam)!=classList[docIndex]:
            errorCount+=1
    print 'the error rate is:',float(errorCount)/len(testSet)   #输出错误率


