__author__ = 'wanghao'

"""
    naive bayes main function
    three example for naive bayes
    author :  wanghao
    email  :  w786058404@163.com
"""

from numpy import *
import bayes

postingList, classVec = bayes.loadDataSet()

vablist = bayes.createVocablist(postingList)

print "Show my vablist\n", vablist

returnVec = bayes.setOfwords2Vec(vablist, ["my", "love", "dog", "happy", "daddy"])

print "the word vec is ", returnVec