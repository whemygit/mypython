#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

def loadDataSet():
    postingList=[["my","dog","has","flea",
                  "problem", "help", "please"], ["maybe", "not", "take"],["my","dog"],["please","go","you"]]
    classVec=[0,1,0,1,0,1]
    return postingList,classVec

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        # print type(set(document))
        vocabSet=vocabSet | set(document)
    return list(vocabSet)

def setofWord2Vec(vocalList,inputSet):
    # print vocalList
    returnVec=[0]*len(vocalList)
    for word in inputSet:
        if word in inputSet:
            returnVec[vocalList.index(word)]=1
        else:print "the word: %s is not in my Vocabulary!" %word
    return returnVec

import bayes1
listOPosts,listClasses=bayes1.loadDataSet()
print listOPosts
myVocabList=bayes1.createVocabList(listOPosts)
print myVocabList

vectors=bayes1.setofWord2Vec(myVocabList, listOPosts[1])
print vectors