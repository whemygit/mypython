#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import happybase

reload(sys)
sys.setdefaultencoding("utf-8")

class pythonHaseTest():
    def __init__(self,hbase_host):
        self.host=hbase_host
        self.connection=happybase.Connection(self.host)

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
        put=table.put('row2',{'cf:a':'value2'})
        print put



if __name__ == '__main__':
    hbase_host='117.78.60.108'
    hbase_connect=pythonHaseTest(hbase_host=hbase_host)
    table_list=hbase_connect.show_tables()
    print table_list[0]
    hbase_connect.select_table_row(table_list[0],'row1')
    hbase_connect.put_data('test')
    row_key_list=['row1','row2']
    hbase_connect.select_table_rows('test',row_key_list)