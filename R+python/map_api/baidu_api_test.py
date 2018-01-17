#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import json
import requests

reload(sys)
sys.setdefaultencoding("utf-8")

def getlnglat():
    url='http://api.map.baidu.com/geocoder/v2/'
    output='json'
    ak='Qk77GopeGV7dPCPAAHpLHG0sl87pGbcV'
    # add='北京市海淀区上地十街10号'
    add = 'null'
    uri=url+'?'+'address='+add+'&output=' + output + '&ak=' + ak
    resp=requests.get(uri)
    res=resp.text
    temp=json.loads(res)
    print type(temp)
    print temp.keys()
    print temp
    print temp['result']['location']
    print temp['result']


if __name__ == '__main__':
    getlnglat()