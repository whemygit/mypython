#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import os
import random
import csv
import collections
import heapq
from operator import itemgetter

reload(sys)
# sys.setdefaultencoding("utf-8")
# u_id=random.randint(1,100)
# it_id=random.randint(1,500)
# score=random.randint(0,5)

def udata_generate():
    with open('my_ratings','w') as fw:
        for i in range(400):
            user_id=random.randint(1,100)
            item_id=random.randint(1,500)
            score=random.randint(0,5)
            fw.write('\x01'.join([str(user_id),str(item_id),str(score)])+'\n')

def idata_generate():
    with open('my_items', 'w') as fw:
        for i in range(1,501):
            item_id = i
            category_id = random.randint(1, 6)
            fw.write('\x01'.join([str(item_id), str(category_id)]) + '\n')

def relative_path(path):
    dirname=os.path.dirname(os.path.realpath('__file__'))
    path=os.path.join(dirname,path)
    return os.path.normpath(path)

def load_udata(path,**kwargs):
    options={
        'fieldnames':('user_id','item_id','rating'),
        'delimiter':'\x01'
    }
    options.update(kwargs)
    parse_int=lambda r,k:int(r[k])

    with open(path,'rb') as users:
        reader=csv.DictReader(users,**options)
        for row in reader:
            row['user_id']=parse_int(row,'user_id')
            row['item_id']=parse_int(row,'item_id')
            row['rating']=parse_int(row,'rating')
            yield row


def load_itdata(path,**kwargs):
    options={
        'fieldnames':('item_id','category_id'),
        'delimiter':'\x01'
    }
    options.update(kwargs)
    parse_int=lambda r,k:int(r[k])

    with open(path,'rb') as items:
        reader=csv.DictReader(items,**options)
        for row in reader:
            row['item_id']=parse_int(row,'item_id')
            row['category_id']=parse_int(row,'category_id')
            yield row

class Recommend(object):
    def __init__(self,udata,itdata):
        self.udata=udata
        self.itdata=itdata
        self.user_info=collections.defaultdict(dict)
        self.item_info={}
        self.load_dataset()
    #prepare_data#######################################################################################################
    def load_dataset(self):
        for user in load_udata(self.udata):
            self.user_info[user['user_id']][user['item_id']]=user

        for item in load_itdata(self.itdata):
            self.item_info[item['item_id']]=item

    #item_analyse#######################################################################################################
    def review_for_item(self,item_id):
        '''
        查看对于特定item_id的item的评论，{'item_id': 162, 'rating': 0, 'user_id': 37}
        :param item_id:
        :return:
        '''
        for review in self.user_info.values():
            if item_id in review:
                yield review[item_id]


    def item_avarage_rating(self):
        '''
        计算每个item的平均评分
        :return: {'item_id': 2, 'rating_num': 1, 'average': 2.0, 'category_id': 6}
        '''
        for item_id in self.item_info:
            ratings=list(r['rating'] for r in self.review_for_item(item_id))
            try:
                average=sum(ratings)/float(len(ratings))
            except ZeroDivisionError:
                continue
            category=self.item_info[item_id]['category_id']
            # yield (item_id,average,len(ratings),category)
            yield {
                'item_id':item_id,
                'average':average,
                'rating_num':len(ratings),
                'category_id':category
            }

    def top_item_rating(self,n=10):
        '''
        前n个平均评价的item
        :param n:
        :return:
        '''
        return heapq.nlargest(n,self.item_avarage_rating(),key=itemgetter('average'))  #itemgetter(1)为排序依据的列索引号


    def review_for_category(self,category_id):
        '''
        给定类的各个评分
        :param category_id:
        :return:{'item_id': 3, 'rating_num': 1, 'average': 5.0, 'category_id': 1}
        {'item_id': 31, 'rating_num': 1, 'average': 4.0, 'category_id': 1}。。。。。。。。。
        '''
        for review in self.item_avarage_rating():
            if category_id==review['category_id']:
                yield review

    def category_average_rating(self):
        '''
        各类的平均评分
        :return:
        '''
        for category_id in range(1, 7):
            ratings = list(r['average'] for r in self.review_for_category(category_id))
            try:
                average_c = sum(ratings) / float(len(ratings))
            except ZeroDivisionError:
                continue
            yield {
                'category_id': category_id,
                'average_c': average_c,
                'rating_num': len(ratings),
            }

    def sort_category_rating(self,n=6):
        '''
        前n类的平均评分
        :param n:
        :return:
        '''
        return heapq.nlargest(n,self.category_average_rating(),key=itemgetter('average_c'))

    #user_analyse#######################################################################################################
    def user_rating_category(self,user_id):
        '''
        特定用户对各类的评分
        :param user_id: 如user_rating_category(1)
        :return: {2: 5.0, 4: 3.0, 6: 4.0}
        '''
        category_rating={}
        for category in range(1,7):
            ratings=0.0
            rating_num=0.0
            for review in self.user_info[user_id].values():
                if self.item_info[review['item_id']]['category_id']==category:
                    ratings+=review['rating']
                    rating_num+=1
            if rating_num!=0:
                average=ratings/rating_num
                category_rating.update({category:average})
        return category_rating

    def all_user_rating_category(self):
        '''
        所有用户对各类的评价
        :return: {1: {2: 5.0, 4: 3.0, 6: 4.0}, 2: {4: 5.0}, 3: {1: 1.0, 2: 2.0, 4:............}
        '''
        user_category_rating={}
        for user_id in self.user_info:
            user_category_rating[user_id]=self.user_rating_category(user_id)
        return user_category_rating

    def user_prefer(self):
        '''
        各位用户为键，各类评分排列为值的字典
        :return: {1: [(2, 5.0), (6, 4.0), (4, 3.0)], 2: [(4, 5.0)], 3: [(4, 5.0), (2,...........}
        '''
        prefer={}
        for user_id in self.all_user_rating_category():
            u_prefer=self.all_user_rating_category()[user_id]
            sort_prefer=sorted(u_prefer.iteritems(),key=itemgetter(1),reverse=True)
            prefer[user_id]=sort_prefer
        return prefer


    def top_user_pref(self,user_id,n=2):
        '''
        返回user_id用户最喜欢的前n类，并且包含每类评分占比权重，model.top_user_pref(1,2)
        :param user_id:
        :param n:
        :return:(1, 2, 0.5555555555555556)
                (1, 6, 0.4444444444444444)
        '''
        pref=self.user_prefer()[user_id]
        sum_rating=0.0
        for i in range(n):
            sum_rating+=pref[i][1]

        for i in range(n):
            pref_percent=pref[i][1]/sum_rating
            # print pref_percent
            yield (user_id,pref[i][0],pref_percent)






if __name__ == '__main__':
    udata=relative_path('my_ratings')
    itdata=relative_path('my_items')
    model=Recommend(udata,itdata)
    # print model.user_info
    # print model.item_info
    # print model.user_info.items()
    # print model.user_info.values()
    # for i in model.review_for_item(18):
    #     print i
    # for i in model.item_avarage_rating():
    #     print i
    # for i in model.top_item_rating(10):
    #     print i
    # for i in model.review_for_category(1):
    #     print i
    # print model.sort_category_rating(6)
    # print model.user_rating_category(1)
    # for i,j in model.all_user_rating_category().items():
    #     print i,j
    print model.user_prefer()[1]
    # for i in model.top_user_pref(1,2):
    #     print i
    # for i in model.user_info.items():
    #     print i
    # for i in model.item_info.items():
    #     print i
    # print model.user_rating_category(100)
    # print model.all_user_rating_category()
    for i in model.top_user_pref(1):
        print i
