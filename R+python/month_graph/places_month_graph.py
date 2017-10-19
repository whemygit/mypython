#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import json
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.font_manager import findSystemFonts
import re

reload(sys)
sys.setdefaultencoding("utf-8")
#解决中文显示为方框的问题
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'

#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

def load_play_time():
    '''
    返回每个景点每月游玩次数的字典
    :return:
    '''
    play_time_dict={}
    with open('D://gitcode/mypython/R+python/word_cloud/desc','r') as fr:
        lines=fr.readlines()
        for line in lines:
            play_time_dict.update({json.loads(line.strip()).get('name'):''})
        for line in lines:
            try:
                play_time_dict[json.loads(line.strip()).get('name')] += '\x01' + str(re.findall(r'\d+',json.loads(line.strip()).get('play_time'))[1])
            except IndexError as e:
                continue
        place__times={}
        for key in play_time_dict:
            place__times.update({key:''})
        for k,v in play_time_dict.items():
            place__times[k]=[{int(i):v.split('\x01').count(i)} for i in set(v.split('\x01')) if i!='']

        place__times_dict={}
        for key in place__times:
            place__times_dict.update({key:{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}})
        for k,v in place__times.items():
            for i in v:
                place__times_dict[k].update(i)
    return place__times_dict

def place__percent():
    place__times_dict=load_play_time()
    cmp_list=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    place__percent_dict={}
    for k,v in place__times_dict.items():
        if cmp(v.values(),cmp_list)==0:
            continue
        else:
            place__percent_dict.update({k: {}})
            percent_list=[100*float(i)/sum(v.values()) for i in v.values()]
            for i,j in enumerate(v):
                place__percent_dict[k].update({j:percent_list[i]})
    return place__percent_dict


def generate_graph():
    place__percent_dict=place__percent()
    for k,v in place__percent_dict.items():
        plt.figure()
        # findSystemFonts(fontpaths='C:\Windows\Fonts\STZHONGS.TTF')
        plt.bar(v.keys(),v.values(),color='darkblue',edgecolor='grey')
        plt.title(k)
        plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],
                    [r'$1$',r'$2$',r'$3$',r'$4$',r'$5$',r'$6$',r'$7$',r'$8$',r'$9$',r'$10$',r'$11$',r'$12$'])
        plt.xlabel('month')
        plt.ylabel('percent')
        # plt.show()
        try:
            plt.savefig('month_bar/'+k+'.jpg')
        except IOError:
            plt.savefig('month_bar'+k.split('/')[0]+k.split('/')[1]+'.jpg')
        plt.close()
        print k
        # break

def generate_graph_times():
    place__percent_dict=load_play_time()
    for k,v in place__percent_dict.items():
        plt.figure()
        # findSystemFonts(fontpaths='C:\Windows\Fonts\STZHONGS.TTF')
        plt.bar(v.keys(),v.values(),color='darkred',edgecolor='grey')
        plt.title(k)
        plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],
                    [r'$1$',r'$2$',r'$3$',r'$4$',r'$5$',r'$6$',r'$7$',r'$8$',r'$9$',r'$10$',r'$11$',r'$12$'])
        plt.xlabel('month')
        plt.ylabel('percent')
        # plt.show()
        try:
            plt.savefig('month_times_bar/'+k+'.jpg')
        except IOError:
            plt.savefig('month_times_bar/'+k.split('/')[0]+k.split('/')[1]+'.jpg')
        plt.close()
        print k
        # break


if __name__ == '__main__':
    generate_graph_times()
    # pp=place__percent()
    # for k,v in pp.items():
    #     print k,v
    # place__times=load_play_time()
    # for k,v in place__times.items():
    #     print k,v.keys(),v.values(),type(v.keys()),type(v.values())

