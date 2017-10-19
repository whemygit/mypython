#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import sys
import json
import matplotlib
from matplotlib import pyplot as plt
import re
reload(sys)
sys.setdefaultencoding("utf-8")
#解决中文显示为方框的问题
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'

#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

class Month_bar(object):
    def __init__(self,data_path):
        self.place_time_dict=self.load_play_time(data_path)
        self.place_percent_dict=self.place_percent_dict_get()
        self.place_quant_dict=self.place_quant_dict_get()


    def load_play_time(self,data_path):
        play_time_dict = {}
        with open(data_path, 'r') as fr:
            lines = fr.readlines()
            for line in lines:
                play_time_dict.update({json.loads(line.strip()).get('name'): ''})
            for line in lines:
                try:
                    play_time_dict[json.loads(line.strip()).get('name')] += '\x01' + str(
                        re.findall(r'\d+', json.loads(line.strip()).get('play_time'))[1])
                except IndexError as e:
                    continue
            place_times = {}
            for key in play_time_dict:
                place_times.update({key: ''})
            for k, v in play_time_dict.items():
                place_times[k] = [{int(i): v.split('\x01').count(i)} for i in set(v.split('\x01')) if i != '']

            place_times_dict = {}
            for key in place_times:
                place_times_dict.update(
                    {key: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}})
            for k, v in place_times.items():
                for i in v:
                    place_times_dict[k].update(i)
        return place_times_dict

    def place_quant_dict_get(self):
        place_times_dict = self.place_time_dict
        cmp_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        place_quant_dict = {}
        for k, v in place_times_dict.items():
            if cmp(v.values(), cmp_list) == 0:
                continue
            else:
                place_quant_dict.update({k:v})
        return place_quant_dict

    def place_percent_dict_get(self):
        place_times_dict = self.place_time_dict
        cmp_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        place_percent_dict = {}
        for k, v in place_times_dict.items():
            if cmp(v.values(), cmp_list) == 0:
                continue
            else:
                place_percent_dict.update({k: {}})
                percent_list = [100 * float(i) / sum(v.values()) for i in v.values()]
                for i, j in enumerate(v):
                    place_percent_dict[k].update({j: percent_list[i]})
        return place_percent_dict

    def generate_graph(self,save_path,percent=False):
        if percent:
            place_percent_dict = self.place_percent_dict
            for k, v in place_percent_dict.items():
                plt.figure()
                # findSystemFonts(fontpaths='C:\Windows\Fonts\STZHONGS.TTF')
                plt.bar(v.keys(), v.values(), color='darkblue', edgecolor='grey')
                plt.title(k)
                plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                           [r'$1$', r'$2$', r'$3$', r'$4$', r'$5$', r'$6$', r'$7$', r'$8$', r'$9$', r'$10$', r'$11$',
                            r'$12$'])
                plt.xlabel('month')
                plt.ylabel('percent')
                # plt.show()
                try:
                    plt.savefig(save_path+'/' + k + '.jpg')
                except IOError:
                    plt.savefig(save_path+'/'+ k.split('/')[0] + k.split('/')[1] + '.jpg')
                plt.close()
                print k
        else:
            place_quant_dict = self.place_quant_dict
            for k, v in place_quant_dict.items():
                plt.figure()
                # findSystemFonts(fontpaths='C:\Windows\Fonts\STZHONGS.TTF')
                plt.bar(v.keys(), v.values(), color='darkblue', edgecolor='grey')
                plt.title(k)
                plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                           [r'$1$', r'$2$', r'$3$', r'$4$', r'$5$', r'$6$', r'$7$', r'$8$', r'$9$', r'$10$', r'$11$',
                            r'$12$'])
                plt.xlabel('month')
                plt.ylabel('percent')
                # plt.show()
                try:
                    plt.savefig(save_path+'/' + k + '.jpg')
                except IOError:
                    plt.savefig(save_path+'/' + k.split('/')[0] + k.split('/')[1] + '.jpg')
                plt.close()
                print k


if __name__ == '__main__':
    datapath='D://gitcode/mypython/R+python/word_cloud/desc'
    save_path = 'class_quantbar_test'
    model=Month_bar(data_path=datapath)
    model.generate_graph(save_path=save_path)