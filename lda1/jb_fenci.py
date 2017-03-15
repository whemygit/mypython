#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass
import os
os.getcwd()
import jieba
f1=open(r"D:\gitcode\mypython\jieba1\news_from_json")
f2=open(r"D:\gitcode\mypython\lda\fenci_result.txt","a")
lines=f1.readlines()
for line in lines:
    line.replace('\t', '').replace('\n', '').replace(' ', '')
    seg_list = jieba.cut(line, cut_all=False)
    a=" ".join(seg_list)
    f2.write(a+"\n")

f1.close()
f2.close()