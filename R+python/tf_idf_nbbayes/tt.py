#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import sys
import re
import time
import json
import torndb
import jieba
reload(sys)
sys.setdefaultencoding("utf-8")

def mysql_connect():
    mysql_par = {'ip': "192.168.0.202:3306",
                 'port': '3306',
                 'database': 'spider',
                 'user': 'suqi',
                 'password': '123456',
                 'charset':'utf8'}

    # mysql_par={'ip':"119.57.93.42",
    #            'port':'3306',
    #            'database':'spider',
    #            'user':'bigdata',
    #            'password':'zhongguangzhangshi'}


    db = torndb.Connection(host=mysql_par.get('ip'),
                           database=mysql_par.get('database'),
                           user=mysql_par.get('user'),
                           password=mysql_par.get('password'),
                           charset=mysql_par.get('charset'),
                           )
    return db


def read_write_data():
    db=mysql_connect()
    select_sql='''SELECT newsid FROM _news_data_copy WHERE classify_tag=3;'''
    select_sql_r= '''SELECT newsid FROM _news_data_copy WHERE classify_tag=3 limit 10;'''
    res=db.query(select_sql)
    a_list=[]
    res_r=db.query(select_sql_r)
    for i in res_r:
        print i.get('newsid')
        a_list.append(i.get('newsid'))
    for t in res:
        s=t.get('newsid') in a_list
        print s
    # print res_r
    # print res
    # for i in res:
    #     print i.get("newsid")
    #     for t in res_r:
    #         print t.get("newsid")
    #         if i.get("newsid")==t.get("newsid"):
    #             print 'yes'




if __name__ == '__main__':
    read_write_data()
