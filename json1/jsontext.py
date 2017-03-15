#encoding=utf-8
#!/usr/bin/env python
# -- coding: utf-8 --
import json
# http://www.cnblogs.com/coser/archive/2011/12/14/2287739.html
#Function:Analyze json script
#Json is a script can descript data structure as xml,
#for detail, please refer to "http://json.org/json-zh.html".

#Note:
#1.Also, if you write json script from python,
#you should use dump instead of load. pleaser refer to "help(json)".

#json file:
#The file content of temp.json is:
#{
# "name":"00_sample_case1",
# "description":"an example."
#}
f = file("D:/myfile/news_test.json");
s = json.load(f)
print s
f.close

#json string:
s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1", "2"]}}')
print s
print s.keys()
print s["name"]
print s["type"]["name"]
print s["type"]["parameter"][1]


help(json)



# encoding
import json

obj = [[1, 2, 3], 123, 123.123, 'abc', {'key1': (1, 2, 3), 'key2': (4, 5, 6)}]
encodedjson = json.dumps(obj)
print repr(obj)
print encodedjson

# decoding
decodejson = json.loads(encodedjson)
print type(decodejson)
print decodejson[4]['key1']
print decodejson