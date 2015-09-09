__author__ = 'wanghao'

"""
    naive bayes main function
    author :  wanghao
    email  :  w786058404@163.com
"""

from numpy import *
import bayes
import FilterMail

postingList, classVec = bayes.loadDataSet()

# get the vablist
vablist = bayes.createVocablist(postingList)
print "Show my vablist\n", vablist
print "-------------------------------"

# get the returnVec
returnVec = bayes.setOfwords2Vec(vablist, ["my", "love", "dog", "happy", "daddy"])
print "the word vec is ", returnVec
print "-------------------------------"
# get the prior probability
trainMat = []
for one in postingList:
    trainMat.append(bayes.setOfwords2Vec(vablist, one))

pa, p1Vec, p0Vec = bayes.trainNB0(trainMat, classVec)
print "the 1 probability is %f, " % pa
print "the each class , each element probability\n", p1Vec, '\n', p0Vec


print "--------------------------------"
bayes.testNB()

print "--------------------------------"
FilterMail.spamTest()