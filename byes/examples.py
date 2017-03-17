#!/usr/bin/env python
# -- coding: utf-8 --
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
if __name__ == '__main__':
    pass

import numpy as np
# pos_neg_idx=np.logical_or(Y=="positive",Y=="negative")
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

def create_ngram_model():
    tfidf_ngram=TfidfVectorizer(ngram_range=(1,3),
                analyzer="word",binary=False)
    help(TfidfVectorizer())
    clf=MultinomialNB()
    pipeline=Pipeline([("vect",tfidf_ngram),("clf",clf)])                 # pipline类允许将向量化处理器和分类器结合到一起，并提供相同的接口
    return pipeline

    # print ngram_range

from sklearn.metrics import precision_recall_curve,auc
# from sklearn.cross_validation import ShuffleSplit              #交叉验证
from sklearn.model_selection import ShuffleSplit

def train_model(clf_factory,X,Y):
    cv=ShuffleSplit(n=len(X),n_iter=10,test_size=0.3,indices=True,random_state=0)

    scores=[]
    pr_scores=[]

    for train, test in cv:
        X_train,y_train=X[train],Y[train]
        X_test,y_test=X[test],Y[test]

        clf=clf_factory()
        clf.fit(X_train,y_train)

        train_score=clf.score(X_train,y_train)
        test_score=clf.score(X_test,y_test)

        scores.append(test_score)
        proba=clf.predict_proba(X_test)

        precision,recall,pr_thresholds=precision_recall_curve(y_test,proba[:,1])

        pr_scores.append(auc(recall,precision))

    summary=(np.mean(scores),np.std(scores),np.mean(pr_scores),np.std(pr_scores))
    print "%.3f\t%.3f\t%.3f\t"%summary


X,Y=load_sanders_data()
pos_neg_index=np.logical_or(Y=="positive",Y=="negative")
X=X[pos_neg_index]
Y=Y[pos_neg_index]
Y=Y=="positive"
train_model(create_ngram_model)

def tweak_lables(Y,pos_sent_list):
    pos=Y==pos_sent_list[0]
    for sent_label in pos_sent_list[1:]:
        pos |=Y==sent_label
        Y=np.zeros(Y.shape[0])
        Y[pos]=1
    return Y

Y=tweak_lables(Y,["positive","negative"])
train_model(create_ngram_model,X,Y,plot=True)


from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score

def grid_search_model(clf_factory,X,Y):
    cv=ShuffleSplit(n=len(x),n_splits=10,test_size=0.3,indices=True,random_state=0)
    param_grid=dict(vect_ngram_range=[(1,1),(1,2),(1,3)],
                    vect_min_df=[1,2],
                    vect_stop_words=[None,"english"],
                    vect_smooth_idf=[False,True],
                    vect_alpha=[0,0.01,0.05,0.1,0.5,1])

    grid_search=GridSearchCV(clf_factory(),
                             param_grid=param_grid,
                             c=cv,
                             score_func=f1_score,
                             verbose=10)

    grid_search.fit(X,Y)
    return grid_search.best_estimator_

#训练
clf=grid_search_model(create_ngram_model,X,Y)
print clf



















