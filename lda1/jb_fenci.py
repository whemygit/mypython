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

#直接分词
f1=open(r"D:\gitcode\mypython\jieba1\news_from_json")
f2=open(r"D:\gitcode\mypython\lda1\fenci_result","w")
lines=f1.readlines()
for line in lines:
    line.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
    seg_list = jieba.cut(line, cut_all=False)
    a=" ".join(seg_list)
    f2.write(a)

f1.close()
f2.close()



#去掉停用词后分词
f1=open(r"D:\gitcode\mypython\jieba1\news_from_json")
f2=open(r"D:\gitcode\mypython\lda1\each_outstop_fenci_result","w")
lines=f1.readlines()
stop = [line.strip().decode('utf-8') for line in open(r"D:\gitcode\mypython\jieba1\stopw.txt").readlines()]
for line in lines:
    line.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
    seg_list = jieba.cut(line, cut_all=False)
    seg_list_outstop = [w for w in seg_list if w not in stop]
    a=" ".join(seg_list_outstop)
    f2.write(a)

f1.close()
f2.close()


