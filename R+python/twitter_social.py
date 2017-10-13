#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import json
import pickle
from matplotlib import pyplot as plt

reload(sys)
sys.setdefaultencoding("utf-8")

def load_twitter_data():
    with open('twitter_data.json','r') as fr:
        load_dict=json.load(fr)
        return load_dict

def key_elements_get(twitterdata):
    # print '标识符:',load_data[1].get('id')
    # print '文本内容:',load_data[0].get('text')
    print 'entities:',load_data[0].get('entities')
    for i in load_data[0].get('entities').get('hashtags'):
        print i
    # print '实体:',load_data[1].get('entities')
    # print '收藏次数',load_data[1].get('favorite_count')
    # print '转推次数', load_data[1].get('retweet_count')
    # print load_data[1].get('retweet_status')
    # for i,j in enumerate(twitterdata):
    #     print i,j.get('status')

def entities_get(twitterdata,n=1):
    '''
    获取指定推文的实体信息,涉及双重列表解析
    :param twitterdata: 全部推文列表
    :param n: 要分析的推文所对应的索引
    :return:
    '''
    statuses=twitterdata
    # 获取各个推文text
    status_texts= [status['text'] for status in statuses]
    # for i in status_text:
    #     print i
    # 获取各个
    sreen_names=[user_mention['screen_name'] for status in statuses for user_mention in status.get('entities').get('user_mentions')]
    hashtags = [hashtag['text'] for status in statuses  for hashtag in status['entities']['hashtags']]
    words = [w for t in status_texts for w in t.split()]
    # print json.dumps(status_texts[0:5],indent=1)
    # print json.dumps(sreen_names[0:5],indent=1)
    # print json.dumps(hashtags[0:5],indent=1)
    # print json.dumps(words[0:5],indent=1)

    #计数。使用counter计算频率分布得到排过序的元素列表
    from collections import Counter


    for item in [words,sreen_names,hashtags]:
        c=Counter(item)
        print c.most_common()[:10]


    #将排序结果格式化成固定宽度的表格格式
    from prettytable import PrettyTable

    for label,data in (('Word',words),
                       ('Screen Name',sreen_names),
                       ('Hashtag',hashtags)):
        pt=PrettyTable(field_names=[label,'count'])
        c=Counter(data)
        [pt.add_row(kv) for kv in c.most_common()[:10]]
        pt.align[label],pt.align['count']='l','r'
        # print pt

    retweets=[
        (status['retweet_count'],
         status['retweeted_status']['user']['screen_name'],
         status['text'])
        for status in statuses
            if status.has_key('retweeted_status')
    ]

    pt=PrettyTable(field_names=['Count','Screen Name','Text'])
    [pt.add_row(row) for row in sorted(retweets,reverse=True)[:5]]
    pt.max_width['Text'] = 50
    pt.align='l'
    # print pt


    print Counter(words)
    print type(Counter(words))
    word_counts = sorted(Counter(words).values(),reverse=True)
    plt.loglog(word_counts)
    plt.ylabel('Freq')
    plt.xlabel('Word Rank')
    plt.show()



if __name__ == '__main__':
    load_data=load_twitter_data()
    # key_elements_get(load_data)
    entities_get(load_data)