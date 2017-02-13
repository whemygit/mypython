#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

db=db = MySQLdb.connect("localhost","root","1","pytest")

cursor=db.cursor()

sql="select * from employee where income>'%d'" % (1000)

try:
	cursor.execute(sql)
	results=cursor.fetchall()
	for row in results:
		fname=row[0]
                lname=row[1];
                age=row[2];
                sex=row[3];
                income=row[4];
		print(fname, lname, age, sex, income)
except:
	print("errr")


db.close()
