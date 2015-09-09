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

# use the bag-of-words model
def setOfwords2Vec(vocablist, inputSet):

    returnVec = [0]*len(vocablist)
    for word in inputSet:
        if word in vocablist:
            returnVec[vocablist.index(word)] += 1
        else:
            print "the word :%s is not in my vocablist" %word

    return returnVec

# train to get the prior probability
def trainNB0(trainMatrix, trainCategory):

    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])

    # 1 probability
    Pa = sum(trainCategory) / float(numTrainDocs)

    #avoid 0
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0AllNum = 2.0
    p1AllNum = 2.0

    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1AllNum += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0AllNum += sum(trainMatrix[i])

    # avoid underflow
    p1Vec = log(p1Num / p1AllNum)  # change log
    p0Vec = log(p0Num / p0AllNum)

    return Pa, p1Vec, p0Vec


# classify the bayes
def classifyNB(classifyVec, p1Vec, p0Vec, Pa):
    # compute each class probability
    p1 = sum(classifyVec * p1Vec) + log(Pa)
    p0 = sum(classifyVec * p0Vec) + log(1-Pa)
    if p1 > p0 :
        return 1
    else:
        return 0

# test the bayes accuracy:
def testNB():
    # load the data
    listPosts, listClasses = loadDataSet()
    # get the dictionaries
    vablist = createVocablist(listPosts)
    # train the bayes to get the prior probability
    trainMat = []
    for each in listPosts:
        trainMat.append(setOfwords2Vec(vablist, each))
    Pa, p1Vec, p0Vec = trainNB0(trainMat, listClasses)
    # test dataset
    testEntry = ['love', 'my', 'dalmation']
    firstDoc = setOfwords2Vec(vablist, testEntry)
    print "the first test class is ", classifyNB(firstDoc,
                                                 p1Vec, p0Vec, Pa)
    testEntry = ['stupid', 'garbage']
    secondDoc = setOfwords2Vec(vablist, testEntry)
    print  "the second test class is ", classifyNB(secondDoc,
                                                   p1Vec, p0Vec, Pa)


























