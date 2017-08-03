#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import csv
import heapq
import operator
from operator import itemgetter

reload(sys)
sys.setdefaultencoding("utf-8")

def load_cities(path,**kwargs):
    '''

    :param path:
    :param kwargs:
    :return: 多个字典，一行为一个字典
    '''
    options={
        'fieldnames':('country','city','english_name','chinese','url'),
        'delimiter':','
    }
    options.update(kwargs)
    with open(path,'rb') as webs:
        reader = csv.DictReader(webs,**options)
        web_num={}
        for row in reader:
            if row['english_name'] in web_num:
                web_num[row['english_name']]+=1
            else:
                web_num[row['english_name']]=1
        return web_num




if __name__ == '__main__':
    file_path="web_list.csv"
    w=load_cities("web_list.csv")
    print w
    t = sorted(w.iteritems(), key=operator.itemgetter(1), reverse=True)
    for i in t:
        print i[0],":",i[1]