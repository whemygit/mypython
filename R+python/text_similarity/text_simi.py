#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import torndb
from gensim import corpora,models,similarities
from textrank4zh import  TextRank4Keyword,TextRank4Sentence
import jieba

reload(sys)
sys.setdefaultencoding("utf-8")

def mysql_connect():
    mysql = {
        "host": "192.168.0.202",
        "port": "3306",
        "database": "spider",
        "password": "123456",
        "user": "suqi",
        "charset":"utf8"
    }

    db = torndb.Connection(host=mysql.get('host'), database=mysql.get('database'),
                           user=mysql.get('user'),
                           password=mysql.get('password'), charset=mysql.get('charset'))
    return db


def text_test():
    with open('user_desc','r') as fr1,open('stopw.txt','r') as fr2:
        lines_1=fr1.readlines()
        lines_2=fr2.readlines()
        for line in lines_1:
            text=line.strip()
            tr4w=TextRank4Keyword()
            tr4w.analyze(text=text,lower=True,window=2)
            print 'keywords:'
            for item in tr4w.get_keywords(20,word_min_len=1):
                print item
            print 'no_stop_words:'
            for item in tr4w.words_no_stop_words:
                print item
            break

            # tr4s=TextRank4Sentence()
            # tr4s.analyze(text=text,lower=True,source='all_filters')
            # print '摘要：'
            # for item in tr4s.get_key_sentences(num=3):
            #     print item.index, item.weight, item.sentence

def gensim_test():
    raw_documents=[
    '0无偿居间介绍买卖毒品的行为应如何定性',
    '1吸毒男动态持有大量毒品的行为该如何认定',
    '2如何区分是非法种植毒品原植物罪还是非法制造毒品罪',
    '3为毒贩贩卖毒品提供帮助构成贩卖毒品罪',
    '4将自己吸食的毒品原价转让给朋友吸食的行为该如何认定',
    '5为获报酬帮人购买毒品的行为该如何认定',
    '6毒贩出狱后再次够买毒品途中被抓的行为认定',
    '7虚夸毒品功效劝人吸食毒品的行为该如何认定',
    '8妻子下落不明丈夫又与他人登记结婚是否为无效婚姻',
    '9一方未签字办理的结婚登记是否有效',
    '10夫妻双方1990年按农村习俗举办婚礼没有结婚证 一方可否起诉离婚',
    '11结婚前对方父母出资购买的住房写我们二人的名字有效吗',
    '12身份证被别人冒用无法登记结婚怎么办？',
    '13同居后又与他人登记结婚是否构成重婚罪',
    '14未办登记只举办结婚仪式可起诉离婚吗',
    '15同居多年未办理结婚登记，是否可以向法院起诉要求离婚'
    ]

    texts=[[word for word in jieba.cut(document, cut_all=True)] for document in raw_documents]
    # print texts
    # print len(texts)
    dictionary = corpora.Dictionary(texts)
    # print dictionary
    # print len(dictionary)
    # for i,j in dictionary.items():
    #     print i,j
    corpus=[dictionary.doc2bow(text) for text in texts]
    # for i in corpus:
    #     print i

    tfidf=models.TfidfModel(corpus)
    corpus_tfidf=tfidf[corpus]
    for i in corpus_tfidf:
        print i

    similarity=similarities.Similarity('Similarity-tfidf-index',corpus_tfidf,num_features=600)
    # for i in similarity:
    #     print i

    test_corpus='15是否可以向法院起诉要求离婚，同居多年未办理结婚登记'
    test_corpus_1 = dictionary.doc2bow(jieba.cut(test_corpus, cut_all=True))
    print test_corpus_1
    vec_tfidf = tfidf[test_corpus_1]
    print vec_tfidf
    print similarity[vec_tfidf]

    # print similarity[corpus_tfidf[0]]
    # flag=False
    # simila=similarity[corpus_tfidf[0]]
    # for i in simila:
    #     if i>0.9:
    #         flag=True
    # print flag





if __name__ == '__main__':
    # db=mysql_connect()
    # print db
    # text_test()
    gensim_test()
