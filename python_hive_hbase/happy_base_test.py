#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import happybase
import random
import timer
import threading
import time

reload(sys)
sys.setdefaultencoding("utf-8")

class pythonHaseTest():
    def __init__(self,hbase_host,hbase_port):
        self.host=hbase_host
        self.connection=happybase.Connection(self.host,port=hbase_port)
        self.table_list=self.show_tables()

    def show_tables(self):
        '''
        获取hbase中所有table的列表
        :return:
        '''
        print self.connection.tables()
        table_list= self.connection.tables()
        return table_list

    def select_table_row(self,table_name,row_key):
        table=self.connection.table(table_name)
        row=table.row(row=row_key)
        print row
        print row['cf:a']

    def select_table_rows(self,table_name,row_key_list):
        table=self.connection.table(table_name)
        rows=table.rows(row_key_list)
        print rows

    def put_data(self,table_name):
        table=self.connection.table(table_name)
        put=table.put('row4',{'cf:a':'value2','cf:b':'value5'})
        print put

    def scan_table(self,table_name):
        table=self.connection.table(table_name)
        for key,data in table.scan():
            print key,data

class PutData():
    def __init__(self,hbase_host):
        self.host=hbase_host
        self.connection=happybase.Connection(self.host)

    def batch_put(self,table_name):
        connect=self.connection
        table_list = connect.tables()
        if table_name in table_list:
            pass
        else:
            connect.create_table(table_name,{"cf1":dict(max_versions=10)})
        table=connect.table(table_name)
        b=table.batch()
        for i in range(100):
            data=random.randint(0,1000)
            b.put('row-%04d'%data,{'cf1:col1':'value-%2d'%data})
            print i,'row-%04d'%data,'cf1:col1:value-%2d'%data
        b.send()

def loopFunc():
    try:
        model.batch_put('batchtest')
    except:
        print 'error'
    global timer
    timer=threading.Timer(5,loopFunc())
    timer.start()




if __name__ == '__main__':
    # hbase_host='117.78.60.108'
    hbase_host='192.168.5.240'
    hbase_connect=pythonHaseTest(hbase_host=hbase_host,hbase_port=9099)
    table_list=hbase_connect.show_tables()
    # print table_list[0]
    # hbase_connect.select_table_row(table_list[0],'row1')
    # hbase_connect.put_data('test')
    # row_key_list=['row1','row2','row3','row4']
    # hbase_connect.select_table_rows('test',row_key_list)
    # hbase_connect.scan_table('test')

    # model=PutData(hbase_host=hbase_host)
    # loopFunc()
    # timer=threading.Timer(20,loopFunc())
    # timer.start()
    # time.sleep(200)
    # timer.cancel()




