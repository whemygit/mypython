#!/usr/bin/env python
# -- coding: utf-8 --
from __future__ import print_function
import requests
from lxml import etree

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

resp=requests.get('http://www.jd.com')
doc_main=etree.HTML(resp.content)
for x in doc_main.xpath('//body/div/div/div/div/ul/li'):
    print (*x.xpath("a/text()")+x.xpath("a/@href"))

# lines=doc_main.xpath('//body/div[5]/div[1]/div[1]/div/ul/li[1]')
# for i, main_cat in enumerate(lines):
#     sub_cat_list=main_cat.xpath('a/text()')
#     print (sub_cat_list)
#     sub_cat_url_list=main_cat.xpath('a/@href')
#     print (sub_cat_url_list)


# resp=requests.get('http://order.jd.com/center/list.action',headers=None)
# print resp.content.decode('gbk')

# if __name__ == '__main__':
#     pass