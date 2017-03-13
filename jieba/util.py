import sys
# import jieba
#  sys.path.append('../')
import jieba.analyse
def extract_tag(fileName,topK):
    content = open(fileName, 'rb').read()
    tags = jieba.analyse.extract_tags(content, topK=topK)
    return tags;


def extract_weight(filname,topK):
    content = open("tag.txt", 'rb').read()
    tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)
    for tag in tags:
        print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))

