#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import urllib
import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time

reload(sys)
sys.setdefaultencoding("utf-8")

# url='http://chihe.sohu.com/'
def get_news_url(url):
    '''
    从主页面获取各新闻URL和title
    :param url: 主页url
    :return: 每条news的url和title
    '''
    m_page=requests.get(url)
    m_content=m_page.content
    bsObj=BeautifulSoup(m_content,'lxml')
    bsObj=bsObj.find_all('h4')
    for news in bsObj:
        url_and_title=news.find_all('a',{'target':'_blank'})
        if url_and_title!=[]:
            new_url=url_and_title[0]['href'].strip()[2:]
            new_title=url_and_title[0].get_text().strip()
            # print new_url
            # print new_title
            yield new_url,new_title

def get_article_content(url):
    '''
    获取每条新闻content，并写入文本
    :param url:
    :return:
    '''
    url_title=get_news_url(url)
    with open("D://myfile/mult_bayes/business", "w") as article_fw:
        for i,j in url_title:
            article_page=requests.get('http://'+i)
            article_content=article_page.content
            bsObj=BeautifulSoup(article_content,'lxml')
            p_tag=bsObj.find_all('p',attrs={})
            ar_con=[]
            for paragraph in p_tag:
                if paragraph.get_text()!='':
                    # print paragraph.get_text()
                    ar_con.append(paragraph.get_text().strip())
            ar_con_str=''.join(ar_con)
            print ar_con_str
            article_fw.write(ar_con_str+'\n')

d={'a':'1','b':'2'}
print d
print d.get('a')
print d['b']


# if __name__ == '__main__':
#     get_article_content('http://business.sohu.com/')
