#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
db=MySQLdb.connect("localhost","root","1","pytest")

cursor=db.cursor()
cursor.execute("select version()")
data=cursor.fetchone()
print(data)
db.close()
