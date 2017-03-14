#encoding=utf-8
# import sys
# sys.path.append('../')

import os
os.getcwd()
os.chdir('D:\gitcode\mypython\jieba')

import jieba
import jieba.analyse

f=open("news_res.txt","rb")
content=f.read()
stop = [line.strip().decode('utf-8') for line in open('stopw.txt').readlines()]
# jieba.analyse.set_stop_words("stopw.txt")
# jieba.analyse.set_idf_path("idf.txt.big")

print content

seg_list = jieba.cut(content,cut_all=False)
# a=",".join(seg_list)
#
# print (a)
# print len(a)
# for s in set(seg_list):
#     print s
b=','.join(list(set(seg_list)-set(stop)))
print b
print len(b)

tags = jieba.analyse.extract_tags(b, topK=29405, withWeight=True)
print len(tags)
for tag in tags:
    print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))

# tags2= jieba.analyse.extract_tags(b, topK=29405)
# print len(tags2)
# for tag in tags2:
#     print tag
