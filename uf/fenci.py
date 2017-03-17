#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

sys.path.append('../')

import jieba
#直接分词——对原文内容分词,结果每行一条新闻
def content_cut_toline(rfilename,wfilename):
    f1=open(rfilename)                 #如：r"D:\gitcode\mypython\jieba1\news_from_json"
    # f2=open(wfilename)                 #如：r"D:\gitcode\mypython\lda1\fenci_result"
    lines=f1.readlines()
    for line in lines:
        line.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
        seg_list = jieba.cut(line, cut_all=False)
        a=" ".join(seg_list)
        with open(wfilename,"a") as f2:
            f2.write(a)

    f1.close()
    f2.close()



#去停分词——对原文内容去掉停用词后分词,结果每行一条新闻
def outstop_cut_toline(rfilename,wfilename,stopwfile):
    f1=open(rfilename)             #如：r"D:\gitcode\mypython\jieba1\news_from_json"
    # f2=open(wfilename)             #如：r"D:\gitcode\mypython\lda1\each_outstop_fenci_result","w"
    lines=f1.readlines()
    stop = [line.strip().decode('utf-8') for line in open(stopwfile).readlines()]                             #如：r"D:\gitcode\mypython\jieba1\stopw.txt"
    for line in lines:
        line.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
        seg_list = jieba.cut(line, cut_all=False)
        seg_list_outstop = [w for w in seg_list if w not in stop]
        a=" ".join(seg_list_outstop)
        with open(wfilename,"a") as f2:
            f2.write(a)

    f1.close()
    # f2.close()


#去停,取关键词分词(带关键词频数)——对原文内容去掉停用词再取关键词后分词,结果每行一条新闻
def keyoutstop_cut_toline(rfilename,wfilename,stopwfile,keywdwfile):
    f1=open(rfilename)             #如：r"D:\gitcode\mypython\jieba1\news_from_json"
    # f2=open(wfilename)             #如：r"D:\gitcode\mypython\lda1\each_outstop_fenci_result","w"
    lines=f1.readlines()
    stop = [line.strip().decode('utf-8') for line in open(stopwfile).readlines()]                             #如：r"D:\gitcode\mypython\jieba1\stopw.txt"
    keywd = [line.strip().decode('utf-8') for line in open(keywdwfile).readlines()]                           # 如：r"D:\gitcode\mypython\jieba1\keywd_seg.txt"
    for line in lines:
        line.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
        seg_list = jieba.cut(line, cut_all=False)
        seg_list_outstop = [w for w in seg_list if w not in stop and w in keywd]
        a=" ".join(seg_list_outstop)
        with open(wfilename,"a") as f2:
            f2.write(a+"\n")

    f1.close()

