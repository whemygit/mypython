#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from os import path
import jieba
from scipy.misc import imread
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

reload(sys)
sys.setdefaultencoding("utf-8")
#http://www.jianshu.com/p/e4b24a734ccc
# http://blog.csdn.net/levy_cui/article/details/51783867
# http://blog.csdn.net/fly910905/article/details/77763086

def load_corpus():
    with open('Yes Minister','r') as fr:
        my_corpus=fr.read()
    return my_corpus


def wc_generate_basic(mycorpus):
    wordcloud=WordCloud(background_color='yellow',font_path='C:\Windows\Fonts\STZHONGS.TTF',max_words=50).generate(mycorpus)
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis('off')
    plt.show()

def wc_generate():
    mycorpus=load_corpus()
    minister_color=imread('fanbingbing.jpg')
    wc=WordCloud(mask=minister_color)
    wordcloud=wc.generate(mycorpus)
    image_colors=ImageColorGenerator(minister_color)
    plt.imshow(wordcloud)
    plt.axis('off')

    # plt.figure()
    plt.imshow(wordcloud.recolor(color_func=image_colors))
    plt.axis('off')
    # plt.show()

    # plt.figure()
    # plt.imshow(minister_color,cmap=plt.cm.gray)
    # plt.axis('off')
    plt.savefig('ss.jpg')
    plt.show()


def fenci():
    with open('little_prince','r') as fr:
        lines=fr.readlines()
        text=''
        stop = [line.strip().decode('utf-8') for line in open('stopw.txt').readlines()]
        for line in lines:
            # print line.strip()
            segs=jieba.cut(line.strip(),cut_all=False)
            text+=' '.join([w for w in segs if w not in stop])
        return text


if __name__ == '__main__':
    # mycorpus = load_corpus()
    # wc_generate_basic(mycorpus)
    wc_generate()
    # fenci()
    # text=fenci()
    # wc_generate_basic(text)