#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import os
import csv
from datetime import *
import collections
import heapq
from operator import itemgetter

reload(sys)
sys.setdefaultencoding("utf-8")

def load_reviews(path,**kwargs):
    options={
        'fieldnames':('userid','movieid','rating',
                      'timestamp'),
        'delimiter':'\t',
    }

    options.update(kwargs)

    parse_date=lambda r,k:date.fromtimestamp(float(r[k]))
    parse_int=lambda r,k:int(r[k])

    with open(path,'rb') as reviews:
        reader = csv.DictReader(reviews,**options)
        for row in reader:
            # print row
            row['movieid']=parse_int(row,'movieid')
            row['userid']=parse_int(row,'userid')
            row['rating']=parse_int(row,'rating')
            row['timestamp']=parse_date(row,'timestamp')
            yield row


def relative_path(path):
    dirname=os.path.dirname(os.path.realpath('__file__'))
    path=os.path.join(dirname,path)
    return os.path.normpath(path)

def load_movies(path,**kwargs):
    '''

    :param path:
    :param kwargs:
    :return: 多个字典，一行为一个字典
    '''
    options={
        'fieldnames':('movieid','title','release','video',
                      'url'),
        'delimiter':'|',
        'restkey':'genre',
    }

    options.update(kwargs)

    parse_date=lambda r,k:datetime.strptime(r[k],'%d-%b-%Y') if r[k] else None
    parse_int=lambda r,k:int(r[k])

    with open(path,'rb') as movies:
        reader = csv.DictReader(movies,**options)
        for row in reader:
            # print row
            row['movieid']=parse_int(row,'movieid')
            row['release']=parse_date(row,'release')
            row['video']=parse_date(row,'video')
            yield row



class MovieLens(object):
    def __init__(self,udata,uitem):
        self.udata=udata
        self.uitem=uitem
        self.movies={}
        self.reviews=collections.defaultdict(dict)
        self.load_dataset()

    def load_dataset(self):
        for movie in load_movies(self.uitem):
            self.movies[movie['movieid']]=movie

        for review in load_reviews(self.udata):
            self.reviews[review['userid']][review['movieid']]=review

    def reviews_for_movie(self,movieid):
        for review in self.reviews.values():
            if movieid in review:
                yield review[movieid]

    def average_reviews(self):
        for movieid in self.movies:
            reviews=list(r['rating'] for r in self.reviews_for_movie(movieid))
            average=sum(reviews)/float(len(reviews))
            yield (movieid,average,len(reviews))

    def top_rated(self,n=10):
        return heapq.nlargest(n,self.average_reviews(),key=itemgetter(1))

    def bayesian_average(self,c=59,m=3):
        for movieid in self.movies:
            reviews=list(r['rating'] for r in self.reviews_for_movie(movieid))
            average=((c*m)+sum(reviews))/float(c+len(reviews))
            yield (movieid,average,len(reviews))

    def top_rated(self,n=10):
        return heapq.nlargest(n,self.bayesian_average(),key=itemgetter(1))



if __name__ == '__main__':
    # load_movies('./ml-100k/u.item')
    data=relative_path('ml-100k/u.data')
    item=relative_path('ml-100k/u.item')
    model=MovieLens(data,item)
    for mid,avg,num in model.top_rated(10):
        title=model.movies[mid]['title']
        print '[%0.3f average rating (%i reviews)] %s' %(avg,num,title)
