#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from multiprocessing import *
import multiprocessing as mp
import threading
import time


reload(sys)
sys.setdefaultencoding("utf-8")

def washer(dishes,output):
    for dish in dishes:
        print 'washing %s dish'%dish
        output.put(dish)

def dryer(input):
    while True:
        dish=input.get()
        print 'drying %s dish'%dish
        input.task_done()

dish_queue=mp.JoinableQueue()
dryer_proc=mp.Process(target=dryer,args=(dish_queue,))
dryer_proc.daemon=True
dryer_proc.start()

dishes=['salad','bread','entree','dessert']


def do_this(what):
    whoami(what)

def whoami(what):
    print 'threading %s says %s' %(threading.current_thread(),what)


if __name__ == '__main__':
    whoami('i am the main program')
    for i in range(4):
        p=threading.Thread(target=do_this,args=('i am function %s' %i,))
        p.start()
    # freeze_support()
    # washer(dishes,dish_queue)
    # dryer(dish_queue)
