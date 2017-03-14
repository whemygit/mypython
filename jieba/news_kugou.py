#encoding=utf-8

import os
os.getcwd()
os.chdir('D:\gitcode\mypython\jieba')

import jieba
import jieba.analyse
# 编码为json格式
import json
from lxml import etree
with open('news_test.html', 'r') as fr, open('news_res.txt', 'w') as fw:
    a = etree.HTML(fr.read())
    doc = a.xpath('//doc')
    for d in doc:
        # art = dict()
        try:
            url = d.xpath('url/text()')[0]
            # print url
            docno = d.xpath('docno/text()')[0]
            contenttitle = d.xpath('contenttitle/text()')[0]
            content = d.xpath('content/text()')[0]
            print content
            # fw=open('news_res.txt', 'w')
            fw.write(content)
            fw.close()
            seg_list=jieba.cut(content)
            print (",".join(seg_list))
            tags = jieba.analyse.extract_tags(content, topK=10,withWeight=True)
            for tag in tags:
                print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))

            # art['url'] = url
            # art['docno'] = docno
            # art['contenttitle'] = contenttitle
            # art['content'] = content
            # # print json.loads(art)
            # fw.write(json.dumps(art))
        except Exception:
            continue


#读入content
# with open('news_res.txt', 'r') as fr:
#     for line in fr.readlines():
#         # print json.loads(line).get('url')
#         print json.loads(line).get('content')