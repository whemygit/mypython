#!/usr/bin/env python
# -- coding: utf-8 --
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


import os
os.chdir('D:/gitcode/mypython/jieba1')
os.getcwd()


from uf import util
# util.content_extract("news_res.txt", True)
util.content_extract('news_from_json.txt', False)
# util.seg_extract("news_res.txt", False)
# util.seg_outstop_extract("news_res.txt", False)