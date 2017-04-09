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





db=mysql_connect()
sql='select * from news_data where id=29'
res=db.query(sql)
print res[0].get('newsTitle')
print res[0].get('newsContent')