#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import json
import jieba
from wordcloud import WordCloud,ImageColorGenerator
from matplotlib import pyplot as plt
from scipy.misc import imread
from matplotlib.font_manager import FontProperties

reload(sys)
sys.setdefaultencoding("utf-8")

def load_comments_1():
    comments_dict={}
    with open('desc_2','r') as fr:
        lines=fr.readlines()
        for line in lines:
            comments_dict.update({json.loads(line.strip()).get('name'):''})
    return comments_dict

def test():
    with open('desc_2','r') as fr,open('user_desc','w') as fw:
        lines=fr.readlines()
        for line in lines:
            name=json.loads(line.strip()).get('name')
            des=json.loads(line.strip()).get('desc_user')
            fw.write(name+'\x01'+des+'\n')


def load_comments():
    comments_dict=load_comments_1()
    with open('desc_2','r') as fr:
        lines=fr.readlines()
        for line in lines:
            # comments_dict.update({json.loads(line.strip()).get('name'):comments_dict[json.loads(line.strip()).get('name')]+'\x01'+json.loads(line.strip()).get('description')})
            comments_dict[json.loads(line.strip()).get('name')]+=json.loads(line.strip()).get('desc_user')
    return comments_dict

def generate_segdict():
    comments_dict=load_comments()
    comment_seg_dict={}
    stop = [line.strip().decode('utf-8') for line in open('stopw.txt').readlines()]
    for place in comments_dict:
        comments=comments_dict[place]
        segs = jieba.cut(comments, cut_all=False)
        text = ' '.join([w for w in segs if w not in stop])
        comment_seg_dict[place]=text
    return comment_seg_dict

def generate_wordcloud():
    comment_seg_dict=generate_segdict()
    for place in comment_seg_dict:
        if comment_seg_dict[place]!='':
            try:
                #white
                # wordcloud = WordCloud(background_color='white',font_path='C:\Windows\Fonts\STZHONGS.TTF',
                #                       max_words=50).generate(comment_seg_dict[place])
                #black
                wordcloud = WordCloud(font_path='C:\Windows\Fonts\STZHONGS.TTF',
                                      max_words=50).generate(comment_seg_dict[place])
                plt.imshow(wordcloud)
                plt.axis('off')
                plt.savefig('pic_black_610/'+place+'.jpg')
                print place
            except:
                print place,'fail to save picture'
                continue



if __name__ == '__main__':
    generate_wordcloud()
    # test()
    # comments=load_comments()
    # print len(comments)
    # print comments[u'故宫']
    # comment_seg_dict=load_comments_1()
    # for i in comment_seg_dict:
    #     print i