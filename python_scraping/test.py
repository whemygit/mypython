#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import python_torndb
reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass



til='aaaaaaaaaa'
db = python_torndb.mysql_connect()
sql='insert into news_data(newsTitle,newsContent) values (%s,%s)'
db.insert(sql,til,sss)