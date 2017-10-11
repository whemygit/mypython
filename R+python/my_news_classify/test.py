#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
with open('stopw.txt','r') as fr:
    lines=fr.readlines()
    print lines
    for line in lines:
        print line
# if __name__ == '__main__':
#     pass