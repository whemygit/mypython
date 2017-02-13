#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

db=MySQLdb.connect("127.0.0.1","root","1","pytest")

cursor=db.cursor()

#sql="""insert into employee (firstname,lastname,age,sex,income)
#values("mac","hahah",20,"M",3456)"""

sql = "INSERT INTO EMPLOYEE(firstname, \
       lastname, age, sex, income) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)

try:
	cursor.execute(sql)
	db.commit()
	print("success")
except:
	print("failed")
	db.rollback()

db.close()
