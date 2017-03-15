#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities
from gensim.models import word2vec

news =word2vec.Text8Corpus(ur"D:\gitcode\mypython\lda\fenci_result.txt",)  # 加载语料
for n in news:
    print n
model =word2vec.Word2Vec(news, size=20)

print model