#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from snownlp import SnowNLP
reload(sys)
sys.setdefaultencoding("utf-8")

s=SnowNLP(u'这个东西还行')
for i in s.sentences:
    print i
for i in s.words:
    print i
for i in s.tags:
    print i[0],i[1]
print s.sentiments

text=u'''
自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
因此，这一领域的研究将涉及自然语言，即人们日常使用的语言，
所以它与语言学的研究有着密切的联系，但又有重要的区别。
自然语言处理并不是一般地研究自然语言，
而在于研制能有效地实现自然语言通信的计算机系统，
特别是其中的软件系统。因而它是计算机科学的一部分。
'''
s1=SnowNLP(text)
for i in s1.keywords(3):
    print i

for i in s1.summary(3):
    print i

for i in s1.sentences:
    print i

doc='文章'

s2=SnowNLP([
    [u'这篇',u'文章'],
    [u'那篇',u'论文'],
    [u'那个']
])

print s2.tf
print s2.idf
# 相似度计算
print s2.sim([doc.decode(encoding='utf-8')])
print s2.sim([u'论文',u'文章'])

if __name__ == '__main__':
    pass