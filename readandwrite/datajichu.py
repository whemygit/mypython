#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

import numpy as np

# a=np.zeros((5,6))
# print a
# print a.shape
# print a.size
# print a[1,1]
# print a[1,:]
# print a[1,]
# print a[1:,]

b=np.array([1,2,3,4])
print b
print b[0]
print type(b[0])
print 'std: ',b.std()
print b.var()
print b.mean()
print b-b.mean()
print (b-b.mean())**2
print sum((b-b.mean())**2)
print (((b-b.mean())**2).mean())**0.5