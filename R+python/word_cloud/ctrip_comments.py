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

def load_comments():
    comments_dict={}
    with open('desc','r') as fr:
        lines=fr.readlines()
        for line in lines:
            comments_dict.update({json.loads(line.strip()).get('name'):''})
        for line in lines:
            comments_dict[json.loads(line.strip()).get('name')]+='\x01'+json.loads(line.strip()).get('description')
            # print json.loads(line.strip()).keys()
            # # print json.loads(line.strip()).get('star')
            # print json.loads(line.strip()).get('description')
            # # print json.loads(line.strip()).get('score_user')
            # # print json.loads(line.strip()).get('score')
            # # print json.loads(line.strip()).get('desc_user')
            # # print json.loads(line.strip()).get('play_time')
            # print json.loads(line.strip()).get('name')
            # # break
    return comments_dict

def generate_segdict():
    comments_dict=load_comments()
    comment_seg_dict={}
    stop = [line.strip().decode('utf-8') for line in open('stopw.txt').readlines()]
    for place in comments_dict:
        text=''
        comments=comments_dict[place].split('\x01')
        for comment in comments:
            segs = jieba.cut(comment, cut_all=False)
            text += ' '.join([w for w in segs if w not in stop])
        comment_seg_dict[place]=text
        # print comment_seg_dict
        # break
    return comment_seg_dict

def generate_wordcloud():
    comment_seg_dict=generate_segdict()
    for place in comment_seg_dict:
        if comment_seg_dict[place]!='':
            print place
            minister_color = imread('mask_pic.jpg')
            wordcloud = WordCloud(background_color='white',font_path='C:\Windows\Fonts\STZHONGS.TTF',
                                  mask=minister_color,max_words=50).generate(comment_seg_dict[place])
            image_colors=ImageColorGenerator(minister_color)
            plt.imshow(wordcloud)
            plt.axis('off')
            plt.imshow(wordcloud.recolor(color_func=image_colors))
            plt.axis('off')
            try:
                plt.savefig('pic_with_mask/'+place+'.jpg')
            except:
                print place,'fail to save picture'
                continue



if __name__ == '__main__':
    generate_wordcloud()