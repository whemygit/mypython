#!/usr/bin/env python
# -- coding: utf-8 --
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

sys.path.append('../')
import jieba
import jieba.analyse
#提取关键词（不带权重）
def extract_tag(fileName,topK):
    content = open(fileName, 'rb').read()
    tags = jieba.analyse.extract_tags(content, topK=topK)
    return tags;

#提取关键词（带权重）
def extract_weight(filname,topK):
    content = open("tag.txt", 'rb').read()
    tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)
    for tag in tags:
        print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))

#从原文内容提取关键词
def content_extract(filename,withWeight=True):
    f=open(filename,"rb")
    content=f.read()

    seg_list = jieba.cut(content,cut_all=False)
    a=",".join(seg_list)
    print len(a)
    tags = jieba.analyse.extract_tags(content, topK=len(a), withWeight=withWeight)
    print len(tags)
    if withWeight==False:
        keywd="\n".join([w for w in tags])
        defile=open("keywd_content.txt","w")
        defile.write(keywd)
        defile.close()
    for tag in tags:
        if withWeight==False:
            print tag
        elif withWeight==True:
            print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))

#分词后提取关键词
def seg_extract(filename,withWeight=True):
    f=open(filename,"rb")
    content=f.read()

    seg_list = jieba.cut(content,cut_all=False)
    a=",".join(seg_list)

    print len(a)

    tags = jieba.analyse.extract_tags(a, topK=len(a), withWeight=withWeight)
    print len(tags)
    if withWeight == False:
        keywd = "\n".join([w for w in tags])
        defile = open("keywd_seg.txt", "w")
        defile.write(keywd)
        defile.close()
    for tag in tags:
        if withWeight == False:
            print tag
        elif withWeight == True:
            print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))

# 分词去掉停用词后提取关键词
def seg_outstop_extract(filename,withWeight=True):
    f=open(filename,"rb")
    content=f.read()
    stop = [line.strip().decode('utf-8') for line in open('stopw.txt').readlines()]

    seg_list = jieba.cut(content,cut_all=False)
    seg_list_outstop=[w for w in seg_list if w not in stop]
    a=",".join(seg_list_outstop)

    print len(a)

    tags = jieba.analyse.extract_tags(a, topK=len(a), withWeight=withWeight)
    print len(tags)
    if withWeight == False:
        keywd = "\n".join([w for w in tags])
        defile = open("keywd_seg_outstop.txt", "w")
        defile.write(keywd)
        defile.close()
    for tag in tags:
        if withWeight == False:
            print tag
        elif withWeight == True:
            print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))



#对每篇提取关键词
def each_news_seg_extract(filename,defilename):
    f=open(filename,"rb")
    lines=f.readlines()


    for line in lines:
        seg_list=jieba.cut(line,cut_all=False)
        a=",".join(seg_list)
        tags = jieba.analyse.extract_tags(a, topK=len(a), withWeight=False)
        keywd = " ".join([w for w in tags])
        df=open(defilename, 'a')
        df.write(keywd+"\n")
        df.close()




