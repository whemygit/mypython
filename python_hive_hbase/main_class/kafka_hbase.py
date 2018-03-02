#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from kafka import KafkaProducer,KafkaConsumer
import happybase
import json
reload(sys)
sys.setdefaultencoding("utf-8")



class kafkaHbase():
    def __init__(self,hbase_host,hbase_port,kafka_host,kafka_port):
        self.hbase_host=hbase_host
        self.hbase_port=hbase_port
        self.hbase_connection=happybase.Connection(self.hbase_host,port=hbase_port)
        self.hbase_table_list=self.show_tables()

        self.kafka_host=kafka_host
        self.kafka_port=kafka_port
        self.kafka_producer=KafkaProducer(bootstrap_servers=self.kafka_host+':'+self.kafka_port)

    def show_tables(self):
        '''
        获取hbase中所有table的列表
        :return:
        '''
        print self.hbase_connection.tables()
        table_list= self.hbase_connection.tables()
        return table_list

    def kafka_produce_msg(self,topic_name,msg):
        producer=self.kafka_producer
        producer.send(topic_name,msg)
        print topic_name,msg



    def kafka_consume_msg(self,topic_name):
        consumer = KafkaConsumer(topic_name, bootstrap_servers='192.168.5.240:9092')
        for msg in consumer:
            print msg.value.decode('utf-8')
            print json.loads(msg.value.decode('utf-8'))
            print type(json.loads(msg.value.decode('utf-8')))

    def kafka_consumer_put_hbase(self,topic_name,table_name):
        hbase_connection=self.hbase_connection
        hbase_table_list=self.hbase_table_list
        if table_name in hbase_table_list:
            pass
        else:
            hbase_connection.create_table(table_name, {"cf1": dict(max_versions=10)})
        table = hbase_connection.table(table_name)

        kafka_consumer = KafkaConsumer(topic_name, bootstrap_servers=self.kafka_host+':'+self.kafka_port)
        for msg in kafka_consumer:

            put = table.put('kafka_test_row', {'cf1:col1':msg.value})
            print msg.value.decode('utf-8')

if __name__ == '__main__':
    hbase_host='192.168.5.240'
    hbase_port=9099
    kafka_host='192.168.5.240'
    kafka_port='9092'
    model=kafkaHbase(hbase_host=hbase_host,hbase_port=hbase_port,kafka_host=kafka_host,kafka_port=kafka_port)

    # model.kafka_produce_msg(topic_name='hbase_kafka_test',msg=json.dumps({'my_key':'my_value'}))
    model.kafka_consumer_put_hbase(topic_name='dict_test',table_name='kafka_test_table')
    # model.kafka_consume_msg(topic_name='dict_test')