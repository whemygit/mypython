#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import os
import jieba
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import  CountVectorizer
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
reload(sys)
sys.setdefaultencoding("utf-8")

def relative_path(path):
    dirname = os.path.dirname(os.path.realpath('__file__'))
    path = os.path.join(dirname, path)
    return os.path.normpath(path)


def news_cut_outstop(news_text):
    stopwd=[line.strip().decode('utf-8') for line in open('D:/gitcode/mypython/R+python/my_news_classify/stopw.txt').readlines()]
    news_text=news_text.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
    seg_list=jieba.cut(news_text,cut_all=False)
    seg_list_outstop=[w for w in seg_list if w not in stopwd]
    return seg_list_outstop

def get_doc_list():
    with open(relative_path('test.txt'),'r') as fr:
        lines=fr.readlines()
        doc_list=[]
        for line in lines:
            # print line.strip()
            line_seg=news_cut_outstop(line)
            line_seg=' '.join(line_seg)
            # print line_seg
            doc_list.append(line_seg)
        return doc_list

def transform_tfidf():
    vec=TfidfVectorizer(lowercase=False,decode_error='ignore')
    doc_tfidf_vec=vec.fit_transform(get_doc_list())
    # for i,j in enumerate(vec.get_feature_names()):
    #     print i,j
    return doc_tfidf_vec

def create_vocablist():
    vocab_set=set([])
    doc_list=get_doc_list()
    for document_seg in doc_list:
        vocab_set=vocab_set | set(document_seg)
    vocab_set=list(vocab_set)
    return vocab_set



if __name__ == '__main__':
    doc_tfidf_vec=transform_tfidf()
    # print type(doc_tfidf_vec)
    print doc_tfidf_vec.shape

    # vocabset=create_vocablist()
    # for i,j in enumerate(vocabset):
    #     print i,j

