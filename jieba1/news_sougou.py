#!/usr/bin/env python
# -- coding: utf-8 --
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


import os
os.chdir('D:\gitcode\mypython\jieba1')


# 解析json格式
import json

with open('news_json', 'r') as fr:
    for line in fr.readlines():
        a=json.loads(line).get('content')
        print a
        fw = open('news_from_json', 'a')
        fw.write(a+"\n")
        fw.close()