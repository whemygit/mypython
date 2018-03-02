#!/usr/bin/env python
# -- coding: utf-8 --
import random
import sys
import csv
import threading
import time
from kafka import KafkaProducer
import json


reload(sys)
sys.setdefaultencoding("utf-8")

producer=KafkaProducer(bootstrap_servers='192.168.5.240:9092')
# csvfile=open('user_log.csv','r')
# reader=csv.reader(csvfile)
#
# for line in reader:
#     gender=line[9]
#     if gender=='gender':
#         continue
#     time.sleep(0.1)
#     producer.send('sex',line[9].encode('utf-8'))

# while True:
#     for i in range(100):
#         print i
#         producer.send('sex',str(i).encode('utf-8'))

def random_gen():
    s=random.randint(1,5)
    return s

def fun_timer():
    for i in range(10):
        radint=str(random_gen())
        # producer.send('sex', radint.encode('utf-8'))
        producer.send('dict_test',json.dumps({i:radint.encode('utf-8')}))
        print json.dumps({i:radint.encode('utf-8')})
    global timer
    timer = threading.Timer(2, fun_timer)
    timer.start()


# timer = threading.Timer(1, fun_timer)
# timer.start()

# if __name__ == '__main__':
#     timer = threading.Timer(1, fun_timer)
#     timer.start()
def myfunc():
    print "send kafka"


def loopFunc():
    try:
        myfunc()
    except:
        print 'error'
    global timer
    timer = threading.Timer(5, loopFunc)
    timer.start()

def loop():
    timer = threading.Timer(1, loopFunc)
    timer.start()

# time.sleep(10) # 15秒后停止定时器
# timer.cancel()

flag = True
def timerUtil():
    if flag:
        print "a"
        time.sleep(2)  # 15秒后停止定时器


if __name__ == '__main__':
    fun_timer()
    # loopFunc()
    # time.sleep(10) # 10秒后停止定时器
    # timer.cancel()
    # timerUtil()
    # time.sleep(10)
    # flag = False