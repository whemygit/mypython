#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import networkx as nx
import unicodecsv as csv
import operator
import matplotlib.pyplot as plt
import community
import requests

import urllib2
from bs4 import BeautifulSoup

from weibo import Client
import urllib

reload(sys)
sys.setdefaultencoding("utf-8")


def baidu_news_spider():
    url='http://news.baidu.com/'
    content = urllib2.urlopen(url).read()
    # print content
    soup = BeautifulSoup(content,"lxml",from_encoding='gbk')
    hotNews = soup.find_all('div',{'class','hotnews'})[0].find_all('li')
    for i in hotNews:
        print i.a.text


def weiboClient():
    APP_KEY = '2149070838' # app key
    APP_SECRET = '73caaf506d849ece3fd319ee099e37eb' # app secret
    CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html' # callback url
    AUTH_URL = 'https://api.weibo.com/oauth2/authorize'
    USERID = 'whemy@sina.com'
    PASSWD = 'wwwmmm555432' #your pw
    client = Client(api_key=APP_KEY,api_secret=APP_SECRET,redirect_uri=CALLBACK_URL)
    referer_url = client.authorize_url
    print "referer url is : %s" % referer_url
    cookies = urllib2.HTTPCookieProcessor()
    opener = urllib2.build_opener(cookies)
    urllib2.install_opener(opener)
    postdata = {"client_id": APP_KEY,
            "redirect_uri": CALLBACK_URL,
            "userId": USERID,
            "passwd": PASSWD,
            "isLoginSina": "0",
            "action": "submit",
            "response_type": "code",
               }
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
               "Host": "api.weibo.com",
               "Referer": referer_url
               }
    req  = urllib2.Request(
       # url = referer_url,
       url=AUTH_URL,
       data = urllib.urlencode(postdata),
       headers = headers
       )
    try:
        resp = urllib2.urlopen(req)
        print "callback url is : %s" % resp.geturl()

        # rr=requests.post(referer_url)
        # print 'rr:',rr.text
        code = resp.geturl()[-32:]
        # code = '3f905ea7699d1db3d64b35fb64184d6d'
        print "code is : %s" %  code
        # 'https://api.weibo.com/oauth2/authorize?redirect_uri=https%3A%2F%2Fapi.weibo.com%2Foauth2%2Fdefault.html&client_id=2149070838'
    except Exception, e:
        print e
    r = client.set_code(code)
    print r
    access_token1 = r.set_token() # The token return by sina
    expires_in = r.expires_in

    print "access_token=" ,access_token1
    print "expires_in=" ,expires_in   # access_token lifetime by second.
    client.set_access_token(access_token1, expires_in)
    return client


def draw_nx():
    G=nx.Graph()
    G.add_edge(1,2)
    nx.draw_networkx(G)
    plt.show()
    T=nx.krackhardt_kite_graph()
    nx.draw_networkx(T)
    plt.show()


if __name__ == '__main__':
    client1=weiboClient()
