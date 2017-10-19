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

class Ctrip_wordcloud(object):
    def __init__(self,data_path,stopwd_path):
        self.comments_dict=self.load_comments(data_path)
        self.stopwd=[line.strip().decode('utf-8') for line in open(stopwd_path).readlines()]
        self.comments_seg_dict=self.get_comment_seg()



    def load_comments(self,data_path):
        comments_dict={}
        with open(data_path,'r') as fr:
            lines=fr.readlines()
            for line in lines:
                comments_dict.update({json.loads(line.strip()).get('name'):''})
            for line in lines:
                comments_dict[json.loads(line.strip()).get('name')] += json.loads(line.strip()).get('desc_user')
        return comments_dict

    def get_comment_seg(self):
        comments_dict=self.comments_dict
        comments_seg_dict={}
        for place,comment in comments_dict.items():
            segs=jieba.cut(comment,cut_all=True)
            text=' '.join([w for w in segs if w not in self.stopwd])
            comments_seg_dict[place]=text
        return comments_seg_dict

    def wordcloud_generate(self,pic_save_path,mask_path=''):
        comments_seg_dict=self.comments_seg_dict
        if mask_path:
            for place in comments_seg_dict:
                if comments_seg_dict[place] != '':
                    print place
                    minister_color = imread(mask_path)
                    try:
                        wordcloud = WordCloud(font_path='C:\Windows\Fonts\STZHONGS.TTF',
                                              mask=minister_color, max_words=50).generate(comments_seg_dict[place])
                    except:
                        continue
                    image_colors = ImageColorGenerator(minister_color)
                    plt.imshow(wordcloud)
                    plt.axis('off')
                    plt.imshow(wordcloud.recolor(color_func=image_colors))
                    plt.axis('off')
                    try:
                        plt.savefig(pic_save_path+'/' + place + '.jpg')
                    except:
                        print place, 'fail to save picture'
                        continue
        else:
            for place in comments_seg_dict:
                try:
                    wordcloud = WordCloud(font_path='C:\Windows\Fonts\STZHONGS.TTF',
                                          max_words=50).generate(comments_seg_dict[place])
                    plt.imshow(wordcloud)
                    plt.axis('off')
                    plt.savefig(pic_save_path+'/' + place + '.jpg')
                    print place
                except:
                    print place, 'fail to save picture'
                    continue



if __name__ == '__main__':
    data_path='desc_2'
    stopwd_path='stopw.txt'
    save_path='class_pic_test'
    mask_path='fanbingbing.jpg'
    model=Ctrip_wordcloud(data_path,stopwd_path)
    model.wordcloud_generate(pic_save_path=save_path,mask_path=mask_path)
