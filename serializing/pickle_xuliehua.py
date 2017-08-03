#!/usr/bin/env python
# -- coding: utf-8 --
import sys
# import pickle
import datetime
import cPickle as pickle


reload(sys)
sys.setdefaultencoding("utf-8")
# now1=datetime.datetime.utcnow()
# print now1
# print type(now1)
# pickled=pickle.dumps(now1)
# now2=pickle.loads(pickled)
# print now2
# print type(now2)

# class Tiny():
#     def __str__(self):
#         return 'tiny'
#
# obj1=Tiny()
# print type(obj1)
# print str(obj1)
# pickled=pickle.dumps(obj1)
# print pickled
# obj2=pickle.loads(pickled)
# print obj2

t1=('this is a string', 42, [1, 2, 3], None)
print t1
p1=pickle.dumps(t1)
print p1
t2=pickle.loads(p1)





# if __name__ == '__main__':
#     pass