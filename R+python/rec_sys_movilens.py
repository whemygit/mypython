#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import numpy as np
import os
import csv
from datetime import *
import collections
import heapq
from operator import itemgetter
from math import sqrt
import pickle

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

    def shared_preferences(self,criticA,criticB):
        if criticA not in self.reviews:
            raise KeyError('could not find critic %s in data' %criticA)
        if criticB not in self.reviews:
            raise KeyError('could not find critic %s in data' %criticB)

        moviesA=set(self.reviews[criticA].keys())
        moviesB=set(self.reviews[criticB].keys())
        shared=moviesA & moviesB

        reviews={}
        for movieid in shared:
            reviews[movieid]=(
                self.reviews[criticA][movieid]['rating'],
                self.reviews[criticB][movieid]['rating']
            )
        return reviews

    def euclidean_distance(self,criticA,criticB,prefs='user'):

        # pref={
        #     'user':self.shared_preferences(A,B),
        #     'movies':self.shared_critices(A,B)
        # }

        if prefs=='user':
            preferences=self.shared_preferences(criticA,criticB)
        elif prefs=='movies':
            preferences=self.shared_critices(criticA,criticB)

        if len(preferences)==0:return 0
        sum_of_squares=sum([pow(a-b,2) for a,b in preferences.values()])
        return 1/(1+sqrt(sum_of_squares))

    def pearson_correlation(self,criticA,criticB,prefs='user'):
        # pref={
        #     'user':self.shared_preferences(A,B),
        #     'movies':self.shared_critices(A,B)
        # }
        # preferences=pref.get(prefs)
        if prefs=='user':
            preferences=self.shared_preferences(criticA,criticB)
        elif prefs=='movies':
            preferences=self.shared_critices(criticA,criticB)

        if len(preferences)==0:return 0
        length=len(preferences)

        sumA=sumB=sumSquareA=sumSquareB=sumProducts=0
        for a,b in preferences.values():
            sumA+=a
            sumB+=b
            sumSquareA +=pow(a,2)
            sumSquareB +=pow(b,2)
            sumProducts +=a*b

        numerator=(sumProducts*length)-(sumA*sumB)
        denominator=sqrt(((sumSquareA*length)-pow(sumA,2))*((sumSquareB*length)-pow(sumB,2)))

        if denominator==0:return 0
        return abs(numerator/denominator)

    def similar_critics(self,user,metric='euclidean',n=None):

        metrics={
            'euclidean':self.euclidean_distance,
            'pearson':self.pearson_correlation
        }

        distance=metrics.get(metric)
        # print distance
        if user not in self.reviews:
            raise KeyError('unknown user, %s' %user)
        if not distance or not callable(distance):
            raise KeyError('unknown or unprogrammed distances metric %s' % metric)

        critics={}
        for critic in self.reviews:
            # print critic,type(critic)
            if critic==user:
                continue
            else:
                critics.update({critic:distance(user,critic)})

        if n:
            return heapq.nlargest(n,critics.items(),key=itemgetter(1))
        return critics

    def predict_ranking(self,user,movie,metric='euclidean',critics=None):
        critics=critics or self.similar_critics(user,metric=metric)
        total=0.0
        simsum=0.0

        for critic, similarity in critics.items():
            if movie in self.reviews[critic]:
                total += similarity*self.reviews[critic][movie]['rating']
                simsum += similarity

        if simsum == 0.0:return 0
        return total/simsum

    def predict_all_rankings(self,user,metric='euclidean',n=None):
        critics=self.similar_critics(user,metric=metric)
        movies={
            movie:self.predict_ranking(user,movie,metric,critics) for movie in self.movies
        }

        if n:
            return heapq.nlargest(n,movies.items(),key=itemgetter(1))
        return movies

    def shared_critices(self,movieA,movieB):
        if movieA not in self.movies:
            raise KeyError('could not find movie %s in data' % movieA)
        if movieB not in self.movies:
            raise KeyError('could not find movie %s in data' % movieB)

        criticsA=set(critic for critic in self.reviews if movieA in self.reviews[critic])
        criticsB = set(critic for critic in self.reviews if movieB in self.reviews[critic])

        shared = criticsA & criticsB

        reviews={}
        for critic in shared:
            reviews[critic]=(
                self.reviews[critic][movieA]['rating'],
                self.reviews[critic][movieB]['rating'],
            )
        return reviews

    def similar_items(self,movie,metric='euclidean',n=None):
        metrics={
            'euclidean':self.euclidean_distance,
            'pearson':self.pearson_correlation
        }
        distance=metrics.get(metric,None)

        if movie not in self.reviews:
            raise KeyError('unknown movie, %s' % movie)
        if not distance or not callable(distance):
            raise KeyError('unknown or unprogrammed distance metric %s' % metric)

        items={}
        for item in self.movies:
            if item==movie:
                continue
            items.update({item:distance(item,movie,prefs='movies')})

        if n:
            return heapq.nlargest(n,items.items(),key=itemgetter(1))
        return items

    def predict_ranking(self,user,movie,metric='euclidean'):
        movies=self.similar_items(movie,metric=metric)
        total=0.0
        simsum=0.0

        for relmovie,similarity in movies.items():
            if relmovie in self.reviews[user]:
                total+=similarity*self.reviews[user][relmovie]['rating']
                simsum+=similarity

        if simsum==0.0:return 0.0
        return total/simsum

    def predict_all_rankings(self,user,metric='euclidean',n=None):

        movies={
            movie:self.predict_ranking(user,movie,metric) for movie in self.movies
        }

        if n:
            return heapq.nlargest(n,movies.items(),key=itemgetter(1))
        return movies

class Recommender(object):
    def __init__(self,udata):
        self.udata=udata
        self.users=None
        self.movies=None
        self.reviews=None
        self.load_dataset()

    def load_dataset(self):
        self.users=set([])
        self.movies=set([])
        for review in load_reviews(self.udata):
            self.users.add(review['userid'])
            self.movies.add(review['movieid'])

        self.users=sorted(self.users)
        self.movies=sorted(self.movies)

        self.reviews=np.zeros(shape=(len(self.users),len(self.movies)))
        for review in load_reviews(self.udata):
            uid=self.users.index(review['userid'])
            mid=self.movies.index(review['movieid'])
            self.reviews[uid,mid]=review['rating']

    def sparsity(self):
        return 1-self.density()

    def density(self):
        nonzero=float(np.count_nonzero(self.reviews))
        return nonzero/self.reviews.size

    @classmethod
    def load(cls,pickle_path):
        with open(pickle_path,'rb') as pkl:
            return pickle.load(pkl)

    def __init__(self,udata,description=None):
        self.udata=udata
        self.users=None
        self.movies=None
        self.reviews=None

        self.build_start=None
        self.build_finish=None
        self.description=None

        self.model=None
        self.features=2
        self.steps=5000
        self.alpha=0.0002
        self.beta=0.02

        self.load_dataset()

    def dump(self,pickle_path):
        with open(pickle_path,'wb') as pkl:
            pickle.dump(self,pkl)



if __name__ == '__main__':
    # for i in load_reviews('./ml-100k/u.data'):
    #     print i
    #     break
    # for i in load_movies('./ml-100k/u.item'):
    #     print i
    #     break
    data=relative_path('ml-100k/u.data')
    item=relative_path('ml-100k/u.item')
    # model=MovieLens(data,item)
    # a= set(model.reviews[1].keys())
    # b = set(model.reviews[2].keys())
    # print a&b
    # rev={}
    # for i in a&b:
    #     rev[i]=(model.reviews[1][i]['rating'],model.reviews[2][i]['rating'])
    #     print rev
    #     for a,b in rev.values():
    #         print pow(a-b,2)
    #     break
    # for k in model.reviews.values():
    #     print k
    #     break
    # for i in model.average_reviews():
    #     print i
    #     print type(i)
    #     break
    # for mid,avg,num in model.top_rated(10):
    #     title=model.movies[mid]['title']
    #     print "[%0.3f average rating (%i reviews)] %s" %(avg,num,title)
    # print model.euclidean_distance(232,532)
    # print model.pearson_correlation(232,532)
    # for item in model.similar_critics(232,metric='euclidean',n=10):
    #     print '%4i: %0.3f' %item
    # print model.similar_critics(232,metric='euclidean')
    # print model.predict_ranking(422,50)
    # print model.predict_ranking(422,50,'pearson')
    # print model.predict_all_rankings(578,'pearson')
    # for mid,rating in model.predict_all_rankings(578,'pearson',10):
    #     print '%0.3f: %s' %(rating,model.movies[mid]['title'])

    # for movie,similarity in model.similar_items(631,'pearson').items():
    #     print '%0.3f: %s' %(similarity,model.movies[movie]['title'])
    # for movie,similarity in model.similar_items(631,metric='pearson').items():
    #     print '%0.3f: %s' %(similarity,model.movies[movie]['title'])
    # print model.predict_ranking(232,52,'pearson')
    # for mid,rating in model.predict_all_rankings(578,'pearson',n=10):
    #     print '%0.3f: %s' %(rating,model.movies[mid]['title'])

    model=Recommender(data)
    print '%0.3f%% sparse' %model.sparsity()
    print '%0.3f%% dense' %model.density()



