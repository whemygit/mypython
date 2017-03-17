#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

import numpy as np

a=np.zeros((5,6))
print a
print a.shape
print a.size
print a[1,1]
print a[1,:]
print a[1,]
print a[1:,]

