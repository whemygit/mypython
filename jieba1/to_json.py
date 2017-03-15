#!/usr/bin/env python
# -- coding: utf-8 --
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


import os
os.getcwd()
os.chdir('D:\gitcode\mypython\jieba1')

# 编码为json格式
import json
from lxml import etree
with open('news_test.html', 'r') as fr:
    a = etree.HTML(fr.read())
    doc = a.xpath('//doc')
    news_num = 0
    for d in doc:
        art = dict()
        news_num=news_num+1
        try:
            url = d.xpath('url/text()')[0]
            docno = d.xpath('docno/text()')[0]
            contenttitle = d.xpath('contenttitle/text()')[0]
            content = d.xpath('content/text()')[0]


            art['url'] = url
            art['docno'] = docno
            art['contenttitle'] = contenttitle
            art['content'] = content

            js_art=json.dumps(art)
            fw=open('news_json', 'a')
            fw.write(js_art+"\n")
            fw.close()
        except Exception:
            continue

print news_num
