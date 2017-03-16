#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass
# http://blog.csdn.net/a_step_further/article/details/51176959

import jieba
from gensim import corpora, models

def get_stop_words_set(file_name):
    with open(file_name,'r') as file:
        return set([line.strip() for line in file])


def get_words_list(file_name, stop_word_file):
    stop_words_set = get_stop_words_set(stop_word_file)
    print "共计导入 %d 个停用词" % len(stop_words_set)
    word_list = []
    with open(file_name, 'r') as file:
        for line in file:
            tmp_list = list(jieba.cut(line.strip(), cut_all=False))
            word_list.append(
                [term for term in tmp_list if str(term) not in stop_words_set])  # 注意这里term是unicode类型，如果不转成str，判断会为假
    return word_list



word_list = get_words_list(r'D:\gitcode\mypython\jieba1\news_from_json', r'D:\gitcode\mypython\jieba1\stopw.txt')  # 列表，其中每个元素也是一个列表，即每行文字分词后形成的词语列表
word_dict = corpora.Dictionary(word_list)  # 生成文档的词典，每个词与一个整型索引值对应
corpus_list = [word_dict.doc2bow(text) for text in word_list]  # 词频统计，转化成空间向量格式
lda = models.ldamodel.LdaModel(corpus=corpus_list, id2word=word_dict, num_topics=10, alpha='auto')
print lda
for a in lda.show_topics():
    print a
    # fw = open(r'D:\gitcode\mypython\lda\output.txt', 'a')
    # fw.write(str(a))
    # fw.close()

output_file = './lda_output.txt'
with open(output_file, 'w') as f:
    for pattern in lda.show_topics():
        print >> f, "%s" % str(pattern[0])+" "+str(pattern[1])


# import os
# os.getcwd()

# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# from gensim import corpora, models, similarities
#
# corpus = [[(0, 1.0), (1, 1.0), (2, 1.0)],
#           [(2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0), (8, 1.0)],
#           [(1, 1.0), (3, 1.0), (4, 1.0), (7, 1.0)],
#           [(0, 1.0), (4, 2.0), (7, 1.0)],
#           [(3, 1.0), (5, 1.0), (6, 1.0)],
#           [(9, 1.0)],
#           [(9, 1.0), (10, 1.0)],
#           [(9, 1.0), (10, 1.0), (11, 1.0)],
#           [(8, 1.0), (10, 1.0), (11, 1.0)]]
#
# tfidf = models.TfidfModel(corpus)
# print tfidf
# vec = [(0, 1), (4, 1)]
# print(tfidf[vec])
# index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=12)
# print index
#
# sims = index[tfidf[vec]]
# print(list(enumerate(sims)))


help(models.ldamodel.LdaModel)