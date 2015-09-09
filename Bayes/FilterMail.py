__author__ = 'wanghao'


"""
    filter spam mails
    author :  wanghao
    email  :  w786058404@163.com
"""
from numpy import *
import bayes


# parse text by regular expression\
def textParse(bigString):
    import re
    reg = re.compile("\\W*")
    listTokens = reg.split(bigString)

    return [tok.lower() for tok in listTokens if len(tok) > 0]

# get the nums of files under the doc
def NumsOfDoc(filepath):
    import os
    if os.path.exists(filepath):
        if ~filepath.endswith('/'):
            filepath += '/'
        fileList = os.listdir(filepath)
        return len(fileList)
    else:
        return 0

# Load the dataSet
def spamTest():
    docList = []
    classList = []
    fullText = []

    # read the mail
    for i in range(1,26):
        wordlist1 = textParse(open('./email/spam/%d.txt' %i).read())
        docList.append(wordlist1)
        fullText.extend(docList)
        classList.append(1)
        wordlist0 = textParse(open('./email/ham/%d.txt' %i).read())
        docList.append(wordlist0)
        fullText.extend(docList)
        classList.append(0)

    # get the dictionary
    vablist = bayes.createVocablist(docList)

    # Random Test dateset
    trainingSet = range(50)
    testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del (trainingSet[randIndex])

    trainMat = []
    trainClasses = []

    # Get the train dateset
    for docIndex in trainingSet:
        trainMat.append(bayes.setOfwords2Vec(vablist, docList[docIndex]))
        trainClasses.append(classList[docIndex])

    pa, p1Vec, p0Vec = bayes.trainNB0(trainMat, trainClasses)

    # test the bayes
    errorCount = 0
    for docIndex in testSet:
        testVec = bayes.setOfwords2Vec(vablist, docList[docIndex])
        result = bayes.classifyNB(testVec, p1Vec, p0Vec, pa)
        if result != classList[docIndex]:
            errorCount += 1
    errorrate = float(errorCount) / len(testSet)
    print "the filter spam mail error rate is %f" %errorrate















