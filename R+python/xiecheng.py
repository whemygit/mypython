#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import os
import json
import re
from pandas import Series,DataFrame
from matplotlib import pyplot as plt
from collections import Counter
from prettytable import PrettyTable

reload(sys)
sys.setdefaultencoding("utf-8")



def relative_path(path):
    dirname=os.path.dirname(os.path.realpath('__file__'))
    path=os.path.join(dirname,path)
    return os.path.normpath(path)

def load_data(path):
    with open(relative_path(path),'r') as fr:
        lines=fr.readlines()
        for line in lines:
            print json.loads(line.strip()).keys()
        #     # print json.loads(line.strip())['score']
            break

        comments=[int(json.loads(line.strip()).get('comment').split('条')[0].split('(')[1]) if json.loads(line.strip()).get('comment')!='(暂无点评)' else int(0) for line in lines]
        rankings = [0 if json.loads(line.strip())['ranking'] == '' else int(re.findall(r'\d+',json.loads(line.strip())['ranking'])[0]) for line in lines]
        stars=[0 if json.loads(line.strip())['star']=='' else int(json.loads(line.strip())['star'].split(':')[1].strip('%;')) for line in lines]
        names=[json.loads(line.strip())['name'] for line in lines]
        levels=[len(re.findall(r'\w',str(json.loads(line.strip())['level']))) for line in lines]
        prices=[int(re.findall(r'\d+',str(json.loads(line.strip())['price']))[0]) if re.findall(r'\d+',str(json.loads(line.strip())['price'])) else 0 for line in lines]
        ctrip_prices=[float(str(json.loads(line.strip())['ctrip_price'])) if json.loads(line.strip())['ctrip_price'] else float(0) for line in lines]
        addresses = [json.loads(line.strip())['address'] for line in lines]
    df_data={'comments':comments,
            'rankings':rankings,
            'stars':stars,
            'names':names,
            'levels':levels,
            'prices':prices,
            'ctrip_prices':ctrip_prices,
            'addresses':addresses}
    df_data=DataFrame(df_data)
    return df_data


class trip_model(object):
    def __init__(self,data_path):
        self.data=load_data(data_path)
        self.place_comments=self.comments_description()
        self.value_0_table=self.value_0_percent()
        self.most_popular=self.most_popular_n()
        self.market_price=self.prices_description(price_type='price')
        self.ctrip_price=self.prices_description(price_type='ctrip_price')


    def value_0_percent(self):
        '''
        绘制所有量化指标的hist
        :return:
        '''
        datas=(('comments',self.data.comments),
        ('stars',self.data.stars),
        ('levels',self.data.levels),
        ('prices',self.data.prices),
        ('ctrip_prices',self.data.ctrip_prices)
        )

        pt=PrettyTable(field_names=['label','value_is_0_num','all_value_num','0_num_percentage'])
        for i,data in enumerate(datas):
            c=Counter(data[1])
            pt.add_row((data[0],c[0],sum(c.values()),float(c[0])/sum(c.values())))     #value为0的元素所占比例

        value_0_table=pt
        return value_0_table


    def hist_counts_graph(self):
        '''
        对于键的数量比较少的指标描述各个键出现的频率，适合用bar图，其中，剔除了键为0时的情况，
        '''
        datas=(
        ('prices',self.data.prices),
        ('ctrip_prices',self.data.ctrip_prices)
        )

        col_num=lambda x:x/2 if x%2 == 0 else int(x/2)+1
        print col_num(len(datas))

        plt.figure()
        for i,data in enumerate(datas):
            c = Counter(data[1])
            plt.subplot(2,col_num(len(datas)),i+1,facecolor='g')
            del c[0]
            plt.hist(c.values())
            plt.title(data[0])

        plt.show()

    def bar_counts_graph(self):
        '''
        对于键的数量比较多的指标描述各个键出现的频率，适合用hist图，其中，剔除了键为0时的情况
        '''
        datas = (
                 ('stars', self.data.stars),
                 ('levels', self.data.levels)
                 )

        col_num=lambda x:x/2 if x%2 == 0 else int(x/2)+1
        print col_num(len(datas))

        plt.figure()
        for i,data in enumerate(datas):
            c = Counter(data[1])
            plt.subplot(2,col_num(len(datas)),i+1,facecolor='b')
            del c[0]
            plt.bar(c.keys(),c.values())
            plt.title(data[0])
        plt.show()

    def comments_description(self):
        comments=self.data['comments']
        place_comments_dict={}
        for i in comments.index:
            place_comments_dict.update({self.data['names'][i]:comments[i]})
        place_comments=place_comments_dict
        return place_comments

    def most_popular_n(self,n=10):
        import operator
        top_popular=sorted(self.place_comments.iteritems(),key=operator.itemgetter(1),reverse=True)
        top_n_popular=top_popular[:n]
        pt = PrettyTable(field_names=['places', 'comments_num'])
        for place in top_n_popular:
            pt.add_row(place)
        most_popular=pt
        return most_popular

    def prices_description(self,price_type='price'):
        if price_type=='price':
            prices=self.data['prices']
        if price_type=='ctrip_price':
            prices=self.data['ctrip_prices']

        c=Counter(prices)
        average_price=float(prices.sum())/(len(prices)-c[0])
        return average_price



if __name__ == '__main__':
    data_path = 'data_xiecheng.json'
    model=trip_model(data_path)
    # print model.data.shape
    # # print model.value_0_table
    # # model.hist_counts_graph()
    # # model.bar_counts_graph()
    # # print model.most_popular
    # # model.prices_description()
    # print model.market_price
    # print model.ctrip_price
    print model.data['addresses']




