#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

db=MySQLdb.connect("127.0.0.1","root","1","pytest")
cursor=db.cursor()
cursor.execute("drop table if exists employee")
sql="""create table employee(
firstname char(20) not null,
lastname char(20),
age int,
sex char(1),
income float)"""

cursor.execute(sql)


db.close()
