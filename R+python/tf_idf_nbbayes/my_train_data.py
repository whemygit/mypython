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
import collections
import json
from sklearn.externals import joblib
reload(sys)
sys.setdefaultencoding("utf-8")

def relative_path(path):
    dirname = os.path.dirname(os.path.realpath('__file__'))
    path = os.path.join(dirname, path)
    return os.path.normpath(path)

def load_corpus(path):
    index=0
    for corpus_file in os.listdir(path):
        index+=1
        yield index,corpus_file

class Tfidf_nbbayes_model():
    def __init__(self,corpus,stopwd):
        self.corpus = corpus
        self.stopwd = stopwd
        self.categroy_dict=dict()
        self.get_category_dict()
        self.doc_list=[]
        self.class_list=[]
        self.get_doc_list()

    def get_category_dict(self):
        for i in load_corpus(self.corpus):
            self.categroy_dict[i[1]]=i[0]

    def news_cut_outstop(self,news_text):
        stopwd=[line.strip().decode('utf-8') for line in open(self.stopwd,'r').readlines()]
        news_text=news_text.replace('\t', '').replace('\n', '').replace(' ', '').replace('，', '')
        seg_list=jieba.cut(news_text,cut_all=False)
        seg_list_outstop=[w for w in seg_list if w not in stopwd]
        return seg_list_outstop

    def get_doc_list(self):
        for corpus in self.categroy_dict:
            with open(relative_path('corpus/'+corpus),'r') as fr:
                lines=fr.readlines()
                for line in lines:
                    line_seg = self.news_cut_outstop(json.loads(line).get('content'))
                    line_seg = ' '.join(line_seg)
                    self.doc_list.append(line_seg)
                self.class_list.extend([self.categroy_dict[corpus]]*len(lines))

    def train_test(self):
        x_train,x_test,y_train,y_test=train_test_split(self.doc_list,self.class_list,test_size=0.1)
        tfidf_vec=TfidfVectorizer(lowercase=False,decode_error='ignore',max_features=500000)
        x_train=tfidf_vec.fit_transform(x_train)
        x_test=tfidf_vec.transform(x_test)
        clf=MultinomialNB().fit(x_train,y_train)
        doc_class_predicted=clf.predict(x_test)
        # print len(y_test)
        # print len(doc_class_predicted)
        print np.mean(doc_class_predicted==y_test)
        # joblib.dump(clf,'train_model.m')
        # clf_load=joblib.load('train_model.m')
        # doc_class_predicted_loadmodel=clf_load.predict(x_test)
        # print np.mean(doc_class_predicted_loadmodel==y_test)
        # joblib.dump(tfidf_vec,'tfidf_vec.m')

    def predict_based_model(self):
        clf_load = joblib.load('train_model.m')
        tfidf_model_load=joblib.load('tfidf_vec.m')
        with open(relative_path('corpus/corpuscaijing'),'r') as fr:
            lines=fr.readlines()
            for line in lines:
                test_vec=[]
                news_content=json.loads(line).get('content')
                line_seg = self.news_cut_outstop(news_content)
                line_seg = ' '.join(line_seg)
                test_vec.append(line_seg)
                content_vec=tfidf_model_load.transform(test_vec)
                print clf_load.predict(content_vec)
                break


    def get_train_data_forspark(self):
        for corpus in self.categroy_dict:
            with open(relative_path('corpus/'+corpus),'r') as fr,open(relative_path('train_data/'+str(self.categroy_dict[corpus])+corpus),'w') as fw:
                lines=fr.readlines()
                for line in lines:
                    if json.loads(line).get('content'):
                        line_seg = self.news_cut_outstop(json.loads(line).get('content'))
                        line_seg = ' '.join(line_seg)
                        fw.write(str(self.categroy_dict[corpus])+','+line_seg+'\n')


    def get_train_data_forspark_other(self):
            with open(relative_path('corpus/_minsheng'),'r') as fr,open(relative_path('train_corpus/9minsheng'),'w') as fw:
                lines=fr.readlines()
                for line in lines:
                    if json.loads(line).get('content'):
                        line_seg = self.news_cut_outstop(json.loads(line).get('content'))
                        line_seg = ' '.join(line_seg)
                        fw.write(str(9)+','+line_seg+'\n')


if __name__ == '__main__':
    corpus_path=relative_path('corpus')
    stopw_path='D:/gitcode/mypython/R+python/my_news_classify/stopw.txt'
    model=Tfidf_nbbayes_model(corpus_path,stopw_path)
    model.get_train_data_forspark_other()
    # print model.class_list
    # print len(model.doc_list)
    # print len(model.class_list)
    # model.train_test()
