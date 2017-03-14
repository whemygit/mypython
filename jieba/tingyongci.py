#encoding=utf-8
import sys
sys.path.append('../')

import os
os.getcwd()
os.chdir('D:\gitcode\mypython\jieba')

import jieba
import jieba.analyse
stop = [line.strip().decode('utf-8') for line in open('stopw.txt').readlines() ]

ll=jieba.cut('明天 台风“尼伯特”可能就要 来啦！',cut_all=False)

# for s in set(ll):
#     print s

print '|'.join(list(set(ll)-set(stop)))