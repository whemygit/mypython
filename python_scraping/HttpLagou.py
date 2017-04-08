__author__ = 'lulei'

def readFile(fileName):
    file = open(fileName, 'rb')
    lines = file.readlines()
    map = {}
    for line in lines:
        line = line.replace("\r\n", "")
        kv = line.split(":", 1)
        map[kv[0]] = kv[1]
    return map

headers = readFile("header.txt")
body = readFile("body.txt")
print body
url = "http://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
#print headers
#print body

import json
import requests


def queryLagou(url, body, headers):
    r = requests.post(url, data=body, headers=headers)
    obj = json.loads(r.text)
    lines = obj["content"]["positionResult"]["result"]
    for line in lines:
        print line["companyShortName"], line["positionName"], line["salary"]


def searchLagou(searchKey, start, end):
    body["kd"] = searchKey
    for i in range(start, end):
        body["pn"] = i
        queryLagou(url, body, headers)
    print "---------------------------------"

searchLagou("python", 20, 30)