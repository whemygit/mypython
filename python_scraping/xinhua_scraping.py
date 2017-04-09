#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import urllib
from bs4 import BeautifulSoup
import requests
import re
import python_torndb

url='http://www.xinhuanet.com/'
def news_get(url,topic):
    resp=requests.get(url)
    resp_c=resp.content
    bsObj=BeautifulSoup(resp_c,'lxml')
    bsObj_news=bsObj.findAll('a',{'href':re.compile('http://news..*/'+topic+'/.*')})
    news_href={}
    for new in bsObj_news:
        news_href[new.get_text()]=new['href']
    return news_href



def news_con_get():
    news_url=news_get(url,'politics')
    db = python_torndb.mysql_connect()
    news_til=[]
    news_con=[]
    for key in news_url:
        new_title=key
        new_url=news_url[key]
        # url_1='http://news.xinhuanet.com/politics/2017-04/09/c_1120775517.htm'
        new_html=requests.get(new_url)
        new_detail=new_html.content
        bsObj=BeautifulSoup(new_detail,'lxml')
        bs=bsObj.select("div > p")
        new_content=''
        for s in bs:
            new_content=new_content+s.get_text()+'\n'
        print 'a'+new_content
        sql='insert into news_data(newsTitle,newsContent) values (%s,%s)'
        db.insert(sql,new_title,new_content)
        news_til.append(new_title)                                              #所有标题组成的列表
        news_con.append(new_content)                                            #所有新闻内容组成的列表
    db.close()
    return news_til,news_con


if __name__ == '__main__':
    # news= news_get(url,'politics')
    # for key in news:
    #     print key,news[key]
    news_con_get()
