#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from similarity_demo import similarityDemo
reload(sys)
sys.setdefaultencoding("utf-8")

raw_documents = [
    '无偿居间介绍买卖毒品的行为应如何定性',
    '吸毒男动态持有大量毒品的行为该如何认定',
    '如何区分是非法种植毒品原植物罪还是非法制造毒品罪',
    '为毒贩贩卖毒品提供帮助构成贩卖毒品罪',
    '将自己吸食的毒品原价转让给朋友吸食的行为该如何认定',
    '为获报酬帮人购买毒品的行为该如何认定',
    '毒贩出狱后再次够买毒品途中被抓的行为认定',
    '虚夸毒品功效劝人吸食毒品的行为该如何认定',
    '妻子下落不明丈夫又与他人登记结婚是否为无效婚姻',
    '一方未签字办理的结婚登记是否有效',
    '夫妻双方1990年按农村习俗举办婚礼没有结婚证 一方可否起诉离婚',
    '结婚前对方父母出资购买的住房写我们二人的名字有效吗',
    '身份证被别人冒用无法登记结婚怎么办？',
    '同居后又与他人登记结婚是否构成重婚罪',
    '未办登记只举办结婚仪式可起诉离婚吗',
    '同居多年未办理结婚登记，是否可以向法院起诉要求离婚',
     '无偿介绍买卖毒品的行为应如何定性',
   '妻子下落不明丈夫又与他人登记结婚是否为无效婚姻',
'%%^%^妻子下落不明丈夫又与他人登记结婚是否为无效婚姻',
    '34^^同居后与人登记结婚是否构成重婚罪888'


]
simi_cla=similarityDemo()
for i in raw_documents:
    flag=simi_cla.similarity(i)
    # flag=simi_cla.gensim_test(i)
    if flag == True:
        print i
        print flag

# if __name__ == '__main__':
#     pass