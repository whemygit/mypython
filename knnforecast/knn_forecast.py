#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import csv
import numpy as np
from numpy import *
import operator

reload(sys)
sys.setdefaultencoding("utf-8")

#打开具有一列数据的csv，读取为向量
def csvfile2list(filename):
    csv_coldata=csv.reader(open(filename))
    row_array_data=[]
    for row in csv_coldata:
        row_array_data.append(float(row[0]))
    row_array_data=np.array(row_array_data)
    return row_array_data

def get_trainset(filename,n):
    '''

    :param filename: 读取的文件路径及文件名称
    :param n: 预测自变量特征数量
    :return: 包括自变量和因变量的训练样本，矩阵为n列的自变量，向量为标签因变量
    '''
    row_data=csvfile2list('mdclose.csv')
    data_len=len(row_data)
    train_len=data_len-n
    dataset=np.zeros((train_len,n+1))
    for i in range(train_len):
        dataset[i]=row_data[i:i+n+1]
    train_data=dataset[:,0:dataset.shape[1]-1]
    train_label=[]
    for i in dataset[:,dataset.shape[1]-1]:
        if i>=0:
            label=1
            train_label.append(label)
        else:
            label=-1
            train_label.append(label)
    return train_data,train_label


def get_rand_testIndex(train_data):
    '''

    :param train_data: 待分割的全样本自变量矩阵
    # :return:1/10的随机测试样本索引，9/10的随机训练样本索引
    '''
    trainIndex = range(train_data.shape[0])
    testIndex = []
    for i in range(int(len(trainIndex) * 0.1)):
        randIndex = int(random.uniform(0, len(trainIndex)))
        del (trainIndex[randIndex])
        testIndex.append(randIndex)
    return trainIndex,testIndex


#k-近邻算法
def knn_classify(inX,trainSet,trainLabels,k):
    trainsetSize=trainSet.shape[0]
    expand_inX=tile(inX,(trainsetSize,1))                             #以inX为基本元素扩展成trainsetSize行，1列的矩阵
    diffMat=expand_inX-trainSet                                       #两矩阵相减
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)                                 #行方向相加
    distances=sqDistances**0.5
    sortedDistIndex=distances.argsort()                               #从小到大排序，对应排序位置的原始向量值索引号，从0开始，如np.array([1,8,3,4]).argsort()，结果为[0 2 3 1]
    classCount={}
    for i in range(k):
        voteILabel=trainLabels[sortedDistIndex[i]]                    #依次找出距离最近的前k个label的索引，依据索引找出对应标签
        classCount[voteILabel]=classCount.get(voteILabel,0)+1
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)     #字典转换为元组列表后倒序排序
    num_max_label=sortedClassCount[0][0]                            #最频繁的项集的标签名
    num_max_num=sortedClassCount[0][1]                              #最频繁的项集的数量
    num_max_num_percent = float(sortedClassCount[0][1])/k                   # 最频繁的项集的数量占比
    print 'in the k nearest neighbors, label ',num_max_label,' is the most one, its number is ',num_max_num,' and its percentage is up to ',num_max_num_percent
    return num_max_label,num_max_num,num_max_num_percent                                #返回最频繁的项集的标签类别

def main():
    train_data, train_label = get_trainset('mdclose.csv', 10)
    trainIndex, testIndex = get_rand_testIndex(train_data)
    trainMat=[];labelList=[]
    for i in trainIndex:
        trainMat.append(train_data[i])
        labelList.append(train_label[i])
    right_count=0
    for j in testIndex:
        num_max_label, num_max_num, num_max_num_percent=knn_classify(train_data[j], array(trainMat), array(labelList), 10)
        if num_max_label==train_label[j]:
            right_count+=1
    print 'the rigth rate is: ',float(right_count)/len(testIndex)



if __name__ == '__main__':
    # train_data,train_label=get_trainset('mdclose.csv',10)
    # trainIndex,testIndex=get_rand_testIndex(train_data)
    # d={'q':1,'w':2}
    # print d.get('q',2)
    # print d.iteritems()
    # print sorted(d.iteritems(),key=operator.itemgetter(1),reverse=True)
    # print sorted(d.iteritems(),key=operator.itemgetter(1),reverse=True)[0][0]
    # print sorted(d.iteritems(),key=operator.itemgetter(1),reverse=True)[0][1]
    main()