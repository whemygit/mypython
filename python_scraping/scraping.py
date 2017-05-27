#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

from urllib import *
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj=BeautifulSoup(html,'lxml')
# print bsObj

#根据标签属性查找所有标签
# nameList=bsObj.find_all("span",{"class","green"})
# print type(nameList)
# for name in nameList:
#     print name.get_text()

#根据标签文本内容查找
nameList=bsObj.find_all(text="the prince")
# print type(nameList)
# print len(nameList)
# for name in nameList:
#     print name

html=urlopen('http://www.pythonscraping.com/pages/page3.html','lxml')
bsObj=BeautifulSoup(html)

for child in bsObj.find('table',{'id':'giftList'}).children:
    print child

# for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:
#     print sibling


