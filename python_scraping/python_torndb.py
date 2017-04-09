#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass
import urllib2
import urllib
from bs4 import BeautifulSoup
import re
import json
import requests
import torndb



def mysql_connect():
    mysql_par={'ip':"127.0.0.1:3306",
               'database':'python',
               'user':'root',
               'password':'123456'}

    db=torndb.Connection(host=mysql_par['ip'],
                         database=mysql_par['database'],
                         user=mysql_par['user'],
                         password=mysql_par['password'])
    return db



#从指定表选择指定字段内容,并将循环中每次读取结果汇总为列表
def mysql_read(tableName,labelName):
    db=mysql_connect()
    sql='select * from '+tableName
    res=db.query(sql)
    pos_label=[]
    for pos in res:
        pos_label.append(pos[labelName])
    return pos_label



mysql_read('position','positionName')