#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

#抓取拉勾网主页职位列表超链接及职位名称
import urllib
from bs4 import BeautifulSoup
import re

def get_html(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

html=get_html('https://www.lagou.com/')
print html

bsObj=BeautifulSoup(html,'lxml')
bsObj_a=bsObj.findAll('a',{'href':re.compile(".*zhaopin/.*/")})
# print type(bsObj_a)
for i in bsObj_a:
    print i
    print i.get_text()
    print i.get('href')

def get_href_zhiwei(url):
    zhaopin={}
    html=get_html(url)
    bsObj=BeautifulSoup(html,'lxml')
    bsObj_a_zhaopin=bsObj.findAll('a',{'href':re.compile(".*zhaopin/.*/")})
    for zhiwei in bsObj_a_zhaopin:
        zw_href=zhiwei.get('href')
        zw_jd=zhiwei.get_text()
        zhaopin[zw_href]=zw_jd
    return zhaopin

zhaopin=get_href_zhiwei('https://www.lagou.com/')

with open('D://myfile//output.txt','w') as fw:
    for key in zhaopin:
        output=key+'|'+zhaopin[key]
        print output
        fw.write(output+'\n')


with open('D://myfile//output.txt') as fr:
    lines=fr.readlines()
    for line in lines:
        arr = line.split('|')
        print arr[0],arr[1]
