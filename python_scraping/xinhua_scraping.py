#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import urllib
from bs4 import BeautifulSoup
import requests
import re

url='http://www.xinhuanet.com/'
def news_get(url,topic):
    resp=requests.get(url)
    resp_c=resp.content
    bsObj=BeautifulSoup(resp_c,'lxml')
    bsObj_news=bsObj.findAll('a',{'href':re.compile('http://news..*/'+topic+'/.*')})
    news_href={}
    for new in bsObj_news:
        news_href[new['href']]=new.get_text()
    return news_href



if __name__ == '__main__':
    news_get(url,'politics')
