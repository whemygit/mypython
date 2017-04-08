#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

#抓取拉勾网指定职位的搜索结果
import urllib2
import urllib
from bs4 import BeautifulSoup
import re
import json
import requests

str = "user_trace_token=20170408144329-bc8877287644418891090fb5beefda55; LGUID=20170408144330-ad501010-1c26-11e7-9d67-5254005c3644; JSESSIONID=A29C1D2D73FD41EC3FAE6CF739975D5F; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=index_search; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3Fcity%3D%25E5%258C%2597%25E4%25BA%25AC%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3Fcity%3D%25E5%258C%2597%25E4%25BA%25AC%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1491633819,1491634078,1491642488; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1491655878; _ga=GA1.2.401448176.1491633819; LGSID=20170408204221-cf2f2a77-1c58-11e7-9d77-5254005c3644; LGRID=20170408205109-09828bdb-1c5a-11e7-bedc-525400f775ce; SEARCH_ID=9bb2c297f8644418b8b54973701416c5"
headers = {'Cookie':str}
url='https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'


def get_data(pn,kd):
    data={'first':'true','pn':pn,'kd':kd}
    return data

def file2dit(filepath):
    with open(filepath,'r') as fr:
        lines=fr.readlines()
        d={}
        for line in lines:
            # print line
            line=line.replace('\n','')
            kv=line.split(':',1)
            d[kv[0]]=kv[1]
        return d


def get_position_res(url,pn,kd):
    html=requests.post(url,data=get_data(pn,kd),headers=file2dit('header.txt'))
    with open('D://myfile/position','a') as fw:
        html_jsObj=json.loads(html.text)
        result=html_jsObj['content']['positionResult']['result']
        for pos_inf in result:
            key_list=['positionName','companyFullName','companySize','positionAdvantage','salary','workYear']
            search_r=[]
            for key in key_list:
                search_r.append(key+'='+pos_inf[key])
            search_r=','.join(search_r)
            print search_r
            fw.write(search_r+'\n')



if __name__ == '__main__':
    for pn in range(1):
        get_position_res(url,pn,'python')
