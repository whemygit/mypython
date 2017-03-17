#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

import os
import numpy as np
import matplotlib
import scipy
import matplotlib.pyplot as plt
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer

def lda_topic_tf(infile,n_topics=2):
        # 存储读取语料 一行预料为一个文档
        corpus = []
        # num = 0
        for line in open(infile, 'r').readlines():
            # print line
            corpus.append(line.strip())
            # num = num + 1
        # print corpus
        # print num

        # 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
        vectorizer = CountVectorizer()
        print vectorizer

        # fit_transform是将文本转为词频矩阵
        X = vectorizer.fit_transform(corpus)

        # 获取词袋模型中的所有词语
        word = vectorizer.get_feature_names()
        analyze = vectorizer.build_analyzer()
        weight = X.toarray()

        # #打印每类文本词频矩阵
        # print 'TF Weight: '
        # for i in range(len(weight)):
        #     for j in range(len(word)):
        #         print weight[i][j],
        #     print '\n'
        print len(weight)
        # print (weight[:5, :5])
        #
        # #打印特征向量文本内容
        print 'Features length: ' + str(len(word))
        # for j in range(len(word)):
        #     print word[j],


        # LDA算法
        print 'LDA:'
        import numpy as np
        import lda
        import lda.datasets
        model = lda.LDA(n_topics=n_topics, n_iter=500, random_state=1)
        model.fit(np.asarray(weight))  # model.fit_transform(X) is also available
        # print np.shape(np.asarray(weight))                                             # 权重矩阵的shape
        topic_word = model.topic_word_  # model.components_ also works

        # 输出主题中的TopN关键词
        word = vectorizer.get_feature_names()
        # print len(word)
        # for w in word:
        #     print w
        print topic_word[:, :3]
        n = 10
        for i, topic_dist in enumerate(topic_word):
            topic_words = np.array(word)[np.argsort(topic_dist)][:-(n + 1):-1]
            print(u'*Topic {}\n- {}'.format(i, ' '.join(topic_words)))

        # 文档-主题（Document-Topic）分布
        doc_topic = model.doc_topic_
        print("type(doc_topic): {}".format(type(doc_topic)))
        print("shape: {}".format(doc_topic.shape))

        # 输出前10篇文章最可能的Topic
        label = []
        for n in range(10):
            topic_most_pr = doc_topic[n].argmax()
            label.append(topic_most_pr)
            print("doc: {} topic: {}".format(n, topic_most_pr))

        # # 计算文档主题分布图
        # import matplotlib.pyplot as plt
        # f, ax = plt.subplots(10, 1, figsize=(8, 8), sharex=True)
        # for i, k in enumerate([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        #     ax[i].stem(doc_topic[k, :], linefmt='r-',
        #                markerfmt='ro', basefmt='w-')
        #     ax[i].set_xlim(-1, 2)  # x坐标下标
        #     ax[i].set_ylim(0, 1.2)  # y坐标下标
        #     ax[i].set_ylabel("Prob")
        #     ax[i].set_title("Document {}".format(k))
        # ax[5].set_xlabel("Topic")
        # plt.tight_layout()
        # plt.show()
















