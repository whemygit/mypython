#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import os
import jieba
import numpy as np
from numpy import *
import random

reload(sys)
sys.setdefaultencoding("utf-8")

def relative_path(path):
    '''
    获取相对路径文件path的绝对路径
    :param path:
    :return:
    '''
    dirname = os.path.dirname(os.path.realpath('__file__'))
    path = os.path.join(dirname, path)
    return os.path.normpath(path)

def load_corpus(path):
    '''
    加载语料库
    :param path: 语料库所在文件路径，该路径下包含多个文档，每个文档类别不同
    :return: 文档名，对应其所属类别组成的元组
    '''
    index=0
    for corpus_file in os.listdir(path):
        index+=1
        yield index,corpus_file

class Newsclassify(object):
    def __init__(self,corpus,stopwd):
        self.corpus=corpus
        self.stopwd=stopwd
        self.doc_list=[]
        self.class_list=[]
        self.vocab_set=[]
        self.get_doc_list()
        self.create_vocablist()

    def news_cut_outstop(self,news_text):
        stopwd=[line.strip().decode('utf-8') for line in open(relative_path('stopw.txt')).readlines()]
        news_text=news_text.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
        seg_list=jieba.cut(news_text,cut_all=False)
        seg_list_outstop=[w for w in seg_list if w not in stopwd]
        return seg_list_outstop

    def get_doc_list(self):
        for file in load_corpus(self.corpus):
            # print file                               #各文件对应类
            with open(self.corpus+'/'+file[1],'r') as fr:
                lines=fr.readlines()
                _class_list=[file[0]]*len(lines)
                for line in lines:
                    self.doc_list.append(self.news_cut_outstop(line))
            self.class_list.extend(_class_list)

    def create_vocablist(self):
        vocab_set=set([])
        for document_seg in self.doc_list:
            vocab_set=vocab_set | set(document_seg)
        self.vocab_set=list(vocab_set)

    def bagOfWords2Vec(self,vocab_set,wordlist):
        words_vec=[0]*len(vocab_set)
        for word in wordlist:
            if word in self.vocab_set:
                words_vec[self.vocab_set.index(word)]+=1
            else:print "the word: %s is not in my Vocabulary!" %word
        return words_vec

    def class_list2class_plist(self):
        class_list_array=array(self.class_list)
        class_p_list = []
        for i in unique(self.class_list):
            p = sum(array([w / i for w in class_list_array if w == i])) / float(len(self.class_list))
            class_p_list.append(p)
        return array(class_p_list)

    def train_nb(self,trainMatrix,trainCategory):
        numTrainDocs = len(trainMatrix)
        numWords = len(trainMatrix[0])
        array_class_p_list = self.class_list2class_plist()
        class_word_Num = np.ones((len(unique(trainCategory)), numWords))  # 每个类别下词汇表中各词数量矩阵初始化值
        Denom = np.ones(len(unique(trainCategory))) + len(unique(trainCategory)) - 1  # 每个类别下词总数向量初始化值
        pVect_array = np.zeros(shape(class_word_Num))
        for i in range(numTrainDocs):
            for j in unique(trainCategory):  # 唯一值列表
                if trainCategory[i] == j:
                    class_word_Num[j - 1] += trainMatrix[i]
                    Denom[j - 1] += sum(trainMatrix[i])
        for j in unique(trainCategory):
            pVect_array[j - 1] = log(class_word_Num[j - 1] / Denom[j - 1])
        return pVect_array, array_class_p_list

    def classifyNB(self,news2Classify, pVect_array, array_class_p_list):
        '''分类函数：计算后验概率，根据概率比较，判断待分类文本应属于概率较大的类
        输入：待分类的文本词向量，训练函数输出的结果,分类标签向量(必须为从1开始的连续序列！！！！！！！！)
        输出：待分类文本所属类别'''
        vocablist_path = relative_path('vocablist')
        vocablist = self.rdfile2list(vocablist_path)
        vec2Classify = array(self.bagOfWords2Vec(vocablist,news2Classify))
        classify_p = np.zeros(len(array_class_p_list))
        for i in range(len(classify_p)):
            classify_p[i] = sum(vec2Classify * pVect_array[i]) + log(array_class_p_list[i])
        classify_p = array(classify_p)
        for j in range(len(unique(self.class_list))):
            if classify_p[j] == classify_p.max():
                classify_result = unique(self.class_list)[j]
        return classify_result

    def train_test(self):
        # train
        training_set=range(len(self.doc_list))
        test_set=[]
        for i in range(int(len(self.doc_list)*0.1)):
            rand_index=int(random.uniform(0,len(training_set)))
            test_set.append(training_set[rand_index])
            del (training_set[rand_index])
        # print test_set
        # print training_set
        train_Mat=[]
        train_classes=[]
        for doc_index in training_set:
            train_Mat.append(self.bagOfWords2Vec(self.vocab_set,self.doc_list[doc_index]))
            train_classes.append(self.class_list[doc_index])
        pVect_array, array_class_p_list = self.train_nb (array(train_Mat), array(train_classes))

        with open("pVect_array", "w") as fw_pVect_array, open("array_class_p_list", "w") as fw_pList,open("vocablist","w") as vocfw:
            for r in range(pVect_array.shape[0]):
                fw_pVect_array.write("\x01".join(str(i) for i in pVect_array[r,:])+'\n')
            fw_pList.write("\x01".join(str(i) for i in array_class_p_list))
            vocfw.write("\x01".join(self.vocab_set))

        # test
        error_count=0
        for doc_index in test_set:
            if self.classifyNB(self.doc_list[doc_index],pVect_array,array_class_p_list) != self.class_list[doc_index]:
                error_count+=1
        print "the error rate is: " , float(error_count) / len(test_set)

    def rdfile2array(self,file_to_array):
        with open(file_to_array, "r") as afr:
            a = afr.read()
            p_array = array([float(w) for w in a.split("\x01")])
        return p_array

    # 将读取的文本转换为矩阵
    def file2matrix(self,filename):
        with open(filename, 'r') as fr:
            lines = fr.readlines()
            numOfLines = len(lines)
            eachline_len = len(lines[0].strip().split('\x01'))
            returnMat = zeros((numOfLines, eachline_len))
            index = 0
            for line in lines:
                line = line.strip()
                listFromLine = line.split('\x01')
                returnMat[index, :] = listFromLine
                index += 1
        return returnMat

    # 将读取的文本转换为列表
    def rdfile2list(self,file_to_array):
        with open(file_to_array, "r") as afr:
            a = afr.read()
            v_list = a.split("\x01")
        return v_list

    def news_classify(self,news_content):
        # vocablist_path=relative_path('vocablist')
        # vocablist=self.rdfile2list('vocablist_path')
        pVect_array_path=relative_path('pVect_array')
        array_class_p_list_path=relative_path('array_class_p_list')
        pVect_array = self.file2matrix(pVect_array_path)  # 各类词库概率矩阵
        array_class_p_list = self.rdfile2array(array_class_p_list_path)  #各类新闻占比向量
        seg_list=self.news_cut_outstop(news_content)
        new_class=self.classifyNB(seg_list,pVect_array,array_class_p_list)
        return new_class





if __name__ == '__main__':
    model=Newsclassify('D://myfile/multclasscorpus','stopw.txt')
    # model.train_test()
    with open('D://myfile/multclasscorpus/business', 'r') as fr:
        lines=fr.readlines()
        for line in lines:
            new_class=model.news_classify(line)
            print new_class


