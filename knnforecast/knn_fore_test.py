#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import csv
import numpy as np
from numpy import *
import operator
import tushare as ts
import knn_forecast as knnf

reload(sys)
sys.setdefaultencoding("utf-8")
# data_all=ts.get_hist_data('600727')

def knn_get_par(share_code):
    '''

    :param share_code: 股票代码,输入参数时一定要加单引号！！！！！！！！！！！！！
    :return:各滞后期情况下的预测正确率
    '''
    period_avg_right_rate={}
    for periods in range(2,20):                                                      #滞后期长度循环
        data_all = ts.get_hist_data(share_code)
        train_data, train_label = knnf.get_trainset(data_all, periods)
        right_rate_list=[]
        for t in range(10):                                                          #随机选取样本，交叉验证次数循环
            trainIndex, testIndex = knnf.get_rand_testIndex(train_data)
            trainMat=[];labelList=[]
            for i in trainIndex:
                trainMat.append(train_data[i])
                labelList.append(train_label[i])
            right_count=0
            for j in testIndex:
                num_max_label, num_max_num, num_max_num_percent=knnf.knn_classify(train_data[j], array(trainMat), array(labelList), 10)
                if num_max_label==train_label[j]:
                    right_count+=1
            # print 'the rigth rate is: ',float(right_count)/len(testIndex)
            right_rate_list.append(float(right_count)/len(testIndex))
        avg_right_rate=mean(right_rate_list)
        # print 'in condition of ',periods,' the average right rate is: ',avg_right_rate
        period_avg_right_rate[periods]=avg_right_rate
    sortedPeravgRate=sorted(period_avg_right_rate.iteritems(),key=operator.itemgetter(1),reverse=True)
    print sortedPeravgRate
    return sortedPeravgRate


def knn_fore_next(share_code):
    '''
    利用训练的模型参数进行预测，预测下一期的涨跌情况
    :param share_code:需要预测的股票代码
    :return:
    '''
    sortedPeravgRate = knn_get_par(share_code)
    lag_num=sortedPeravgRate[0][0]
    # print lag_num
    right_rate=sortedPeravgRate[0][1]
    data_all = ts.get_hist_data(share_code)
    train_data, train_label = knnf.get_trainset(data_all, lag_num)
    # print data_all['close'][-(lag_num):]
    num_max_label, num_max_num, num_max_num_percent = knnf.knn_classify(data_all['close'][-(lag_num):], array(train_data),
                                                                        array(train_label), 10)
    if num_max_label==1:
        fresult='上涨'
    else:
        fresult='下跌'
    print 'in the result of the labels,the most one is: ',num_max_label,\
        ' and its percentage is up to: ',num_max_num_percent,' As a result,the forecast result is: ',fresult
    return num_max_label, num_max_num, num_max_num_percent,fresult


if __name__ == '__main__':
    # print data_all
    knn_fore_next('600727')
    knn_fore_next('603701')


