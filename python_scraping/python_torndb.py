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
import MySQLdb



def mysql_connect():
    # mysql_par={'ip':"127.0.0.1:3306",
    #            'database':'python',
    #            'user':'root',
    #            'password':'123456'}

    mysql_par = {'ip': "192.168.0.202",
                 'port': '3306',
                 'database': 'spider',
                 'user': 'root',
                 'password': 'neiwang-zhongguangzhangshi'}

    db=torndb.Connection(host=mysql_par['ip'],
                         database=mysql_par['database'],
                         user=mysql_par['user'],
                         password=mysql_par['password'])
    return db





db=mysql_connect()
sql='select * from news_data'
# res=db.query(sql)
# # print len(res)
# print res[0].get('title')
# print res[0].get('news_date')

delete_sql='''DELETE FROM syd WHERE id=1323;'''
print delete_sql
r=db.execute(delete_sql)
print r