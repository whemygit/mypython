#!/usr/bin/env python
# -- coding: utf-8 --
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# import os
# os.chdir('D:/gitcode/mypython/jieba1')
# os.getcwd()


from uf import util
# util.content_extract("news_res.txt", True)
# util.content_extract('news_from_json.txt', False)
# util.seg_extract("news_res.txt", False)
# util.seg_outstop_extract("news_res.txt", False)
# util.each_news_seg_extract(r"D:\gitcode\mypython\jieba1\news_from_json",r"D:\gitcode\mypython\lda1\each_nkeys_fenci_result")
# util.each_news_seg_outstop_extract(r"D:\gitcode\mypython\jieba1\news_from_json",r"D:\gitcode\mypython\lda1\each_nkeys_outstop_fenci_result")


from uf import lda_topic_func
lda_topic_func.lda_topic_tf('D://gitcode/mypython/lda1/each_outstop_fenci_result',n_topics=2)