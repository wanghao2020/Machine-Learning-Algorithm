__author__ = 'wanghao'


"""
    implement of naive bayes
    three example for naive bayes
    author :  wanghao
    email  :  w786058404@163.com
"""

from numpy import *

#define a little word list (posted by people)
def loadDataSet():

    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food','stupid']
    ]
    classVec = [0, 1, 0, 1, 0, 1]

    return postingList, classVec

# create vocablist
def createVocablist(dataset):

    vocabset = set([])
    for document in dataset:
        vocabset = vocabset | set(document)

    return list(vocabset)

# set the wordvec by the vocablist
def setOfwords2Vec(vocablist, inputSet):

    returnVec = [0]*len(vocablist)
    for word in inputSet:
        if word in vocablist:
            returnVec[vocablist.index(word)] = 1
        else:
            print "the word :%s is not in my vocablist" %word

    return returnVec

#naive bayes train
def trainNB0(trainMatrix, trainCategory):

    numTrainDocs = len(trainMatrix)











