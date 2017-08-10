#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    with open('D:/gitcode/mypython/R+python/tf_idf_nbbayes/train_corpus/9minsheng', 'rb') as fr:
        lines=fr.readlines()
        print len(lines)
        for line in fr.readline():
            # print 1
            print line