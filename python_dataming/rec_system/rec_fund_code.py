#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import re
import torndb
reload(sys)
sys.setdefaultencoding("utf-8")

'''
用create_engine建立连接，连接地址的意思依次为“数据库格式（mysql）+程序名（pymysql）+账号密码@地址端口/数据库名（test）”，最后指定编码为utf8；
all_gzdata是表名，engine是连接数据的引擎，chunksize指定每次读取1万条记录。这时候sql是一个容器，未真正读取数据。
'''
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/pythondata?charset=utf8')
sql = pd.read_sql('select * from all_gzdata limit 100', engine, chunksize = 10)

# engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/mysql?charset=utf8')
# sql = pd.read_sql('select * from user', engine, chunksize = 2)

# counts = [ i['fullURLId'].value_counts() for i in sql] #逐块统计
# counts = pd.concat(counts).groupby(level=0).sum() #合并统计结果，把相同的统计项合并（即按index分组并求和）
# counts=counts.reset_index() #重新设置index，将原来的index作为counts的一列。
# counts.columns=['index','num'] #重新设置列名，主要是第二列，默认为0
# counts['type']=counts['index'].str.extract('(\d{3})')
# counts_=counts[['type','num']]
# counts_=counts_.groupby('type').sum()

def count107(i): #自定义统计函数
    j = i[['fullURL']][i['fullURLId'].str.contains('107')].copy() #找出类别包含107的网址
    j['type'] = None #添加空列
    j['type'][j['fullURL'].str.contains(r'info/.+?/')] = u'知识首页'
    j['type'][j['fullURL'].str.contains(r'info/.+?/.+?')] = u'知识列表页'
    j['type'][j['fullURL'].str.contains(r'/\d+?_*\d+?\.html')] = u'知识内容页'
    return j['type'].value_counts()

counts2=[count107(i) for i in sql]
counts2=pd.concat(counts2).groupby(level=0).sum()
# print counts2
# c = [i['realIP'].value_counts() for i in sql] #分块统计各个IP的出现次数
# count3 = pd.concat(c).groupby(level = 0).sum() #合并统计结果，level=0表示按index分组
# count3 = pd.DataFrame(count3) #Series转为DataFrame
# count3[1] = 1 #添加一列，全为1
# count3.groupby(0).sum() #统计各个“不同的点击次数”分别出现的次数

if __name__ == '__main__':
    # counts2=[count107(i) for i in sql]
    # counts2=pd.concat(counts2).groupby(level=0).sum()
    print counts2
    # print count3
