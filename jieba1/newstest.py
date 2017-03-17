#!/usr/bin/env python
# -- coding: utf-8 --
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# import os
# os.chdir('D:/gitcode/mypython/jieba1')
# os.getcwd()

#提取关键词
from uf import util
# util.content_extract("news_res.txt", True)
# util.content_extract('news_from_json.txt', False)
util.seg_extract("news_from_json", False)
# util.seg_outstop_extract("news_res.txt", False)
# util.each_news_seg_extract(r"D:\gitcode\mypython\jieba1\news_from_json",r"D:\gitcode\mypython\lda1\each_nkeys_fenci_result")
# util.each_news_seg_outstop_extract(r"D:\gitcode\mypython\jieba1\news_from_json",r"D:\gitcode\mypython\lda1\each_nkeys_outstop_fenci_result")

#分词
# from uf import fenci
# fenci.keyoutstop_cut_toline(r"D:\gitcode\mypython\jieba1\news_from_json",r"D:\gitcode\mypython\lda1\each_keyoutstop_fenci_result",r"D:\gitcode\mypython\jieba1\stopw.txt",r"D:\gitcode\mypython\jieba1\keywd_seg.txt")
# fenci.content_cut_toline(r"D:\gitcode\mypython\jieba1\news_from_json",r"D:\gitcode\mypython\lda1\fenci_result")

# #lda计算
# from uf import lda_topic_func
# lda_topic_func.lda_topic_tf('D://gitcode/mypython/lda1/each_keyoutstop_fenci_result',n_topics=10)