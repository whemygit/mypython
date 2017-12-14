#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import pandas as pd
import jieba


reload(sys)
sys.setdefaultencoding("utf-8")

# # 读取原始数据
# inputfile=u'D:\myfile\pythondm\图书配套数据、代码\chapter15\demo\data\huizong.csv'
# outputfile='meidi_jd.txt'
# data=pd.read_csv(inputfile,encoding='utf8')
# data=data[[u'评论']][data[u'品牌']==u'美的']
# data.to_csv(outputfile,index=False)

# 去重
# inputfile='meidi_jd.txt'
# outputfile='meidi_jd_process_1.txt'
# data=pd.read_csv(inputfile,encoding='utf8')
# l1=len(data)
# data=pd.DataFrame(data[u'评论'].unique())
# l2=len(data)
# data.to_csv(outputfile,index=False,header=False,encoding='utf8')
# print u'删除了%s条评论'%(l1-l2)


#删除前缀评分代码
# inputfile1=u'D:\myfile\pythondm\图书配套数据、代码\chapter15\demo\data\meidi_jd_process_end_负面情感结果.txt'
# inputfile12=u'D:\myfile\pythondm\图书配套数据、代码\chapter15\demo\data\meidi_jd_process_end_正面情感结果.txt'
#
# outputfile1='meidi_jd_neg.txt'
# outputfile2='meidi_jd_pos.txt'
#
# data1=pd.read_csv(inputfile1,encoding='utf8',header=None)
# data2=pd.read_csv(inputfile12,encoding='utf8',header=None)
#
#
# data1=pd.DataFrame(data1[0].str.replace('.*?\d+?\t ',''))
# data2=pd.DataFrame(data2[0].str.replace('.*?\d+?\t ',''))
# # print data2
#
# data1.to_csv(outputfile1,index=False,header=False,encoding='utf8')
# data2.to_csv(outputfile2,index=False,header=False,encoding='utf8')

# 分词代码
# inputfile1=u'meidi_jd_neg.txt'
# inputfile2=u'meidi_jd_pos.txt'
# outputfile1='meidi_jd_neg_cut.txt'
# outputfile2='meidi_jd_pos_cut.txt'
#
# data1=pd.read_csv(inputfile1,encoding='utf8',header=None)
# data2=pd.read_csv(inputfile2,encoding='utf8',header=None)
#
# mycut=lambda s: ' '.join(jieba.cut(s))
# data1=data1[0].apply(mycut)
# data2=data2[0].apply(mycut)
#
# data1.to_csv(outputfile1,index=False,header=False,encoding='utf8')
# data2.to_csv(outputfile2,index=False,header=False,encoding='utf8')


# LDA模型
negfile='meidi_jd_neg_cut.txt'
posfile='meidi_jd_pos_cut.txt'
stoplist=u'D:\myfile\pythondm\图书配套数据、代码\chapter15\demo\data\stoplist.txt'

neg=pd.read_csv(negfile,header=None)
pos=pd.read_csv(posfile,header=None)
stop = pd.read_csv(stoplist, encoding = 'utf-8', header = None, sep = 'tipdm')
stop= [' ', ''] +list(stop[0])

neg[1]=neg[0].apply(lambda s:s.split(' '))
neg[2]=neg[1].apply(lambda x: [i for i in x if i not in stop])
pos[1]=pos[0].apply(lambda s:s.split(' '))
pos[2]=pos[1].apply(lambda x: [i for i in x if i not in stop])

from gensim import corpora,models
neg_dict=corpora.Dictionary(neg[2])
neg_corpus=[neg_dict.doc2bow(i) for i in neg[2]]
neg_lda=models.LdaModel(neg_corpus,num_topics=3,id2word=neg_dict)
for i in range(3):
    print neg_lda.print_topic(i)

pos_dict=corpora.Dictionary(neg[2])
pos_corpus=[pos_dict.doc2bow(i) for i in neg[2]]
pos_lda=models.LdaModel(pos_corpus,num_topics=3,id2word=pos_dict)
for i in range(3):
    print pos_lda.print_topic(i)

if __name__ == '__main__':
    pass