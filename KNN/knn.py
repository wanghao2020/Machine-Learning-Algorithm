__author__ = 'wanghao'

"""
    simple use the knn without kd tree
    author :  wanghao
    email  :  w786058404@163.com
"""

from numpy import *
import operator
import os

# create dataset

def createDataSet():

    groups = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']

    return groups, labels

# create datasize from txt or other file

def filetoMatrix(filename):

    fr = open(filename)
    arraylines = fr.readlines()
    size = len(arraylines)
    returnMatrix = zeros((size, 3))   #the num of feature is 3 in txt, you can change
    labelsVector = []
    index = 0
    for line in arraylines:
        oneline = line.strip()
        lineSplitArray = oneline.split('\t')
        returnMatrix[index, :] = lineSplitArray[0:3]
        labelsVector.append(int(lineSplitArray[-1]))
        index += 1

    return returnMatrix, labelsVector

# data prepare "Normalization"
def autoNorm(dataset):

    minval = dataset.min(0)
    maxval = dataset.max(0)
    range = maxval - minval
    size = dataset.shape[0]
    normDataSet = (dataset - tile(minval, (size, 1))) / tile(range, (size, 1))

    return normDataSet, range, minval



# simple knn classify

def classify0(inx, dataset, labels, k):

    datasize = dataset.shape[0]
    diff = tile(inx, (datasize, 1)) - dataset
    sqDiff = diff**2
    sqDistances = sqDiff.sum(axis = 1)
    Distances = sqDistances**0.5
    sortedDistancesIndex = Distances.argsort()
    classcount = {}
    for i in range(k):
        votelabel = labels[sortedDistancesIndex[i]]
        classcount[votelabel] = classcount.get(votelabel, 0) + 1
    sortedclassCount = sorted(classcount.iteritems(), key=operator.itemgetter(1), reverse=True)

    return sortedclassCount[0][0]


# test the knn with datedata , get the result

def classifytest():

    hoRatio = 0.1
    groups, labels = filetoMatrix('./datingTestSet2.txt')
    size = groups.shape[0]
    testnum = int(size * hoRatio)
    normGroups, ranges, minval = autoNorm(groups)
    errornum = 0.0

    for i in range(testnum):
        resultlabel = classify0(normGroups[i, :], normGroups[testnum:size, :],
                                labels[testnum:size], 3)
        print "the %d classifier result is: %d, the real result is %d" %(i,resultlabel, labels[i])

        if (resultlabel != labels[i]):
            errornum += 1.0
    print "the error ratio is %f" %(errornum/float(testnum))


# convert one txt file to vector
def img2vector(filename):

    f = open(filename)
    returnMatrix = zeros((1,1024))
    for i in range(32):
        line = f.readline()
        for j in range(32):
            returnMatrix[ 0, 32*i + j] = int(line[j])

    return returnMatrix

# test the hand writing img . get the result

def handWritingClassifyTest():

    hwlabels = []
    hwTrainfiles = os.listdir('./trainingDigits')
    hwTrainNum = len(hwTrainfiles)
    TrainMatrix = zeros((hwTrainNum, 1024))

    for i in range(hwTrainNum):
        file = hwTrainfiles[i]
        filename = file.split('.')[0]
        filelabel = int(filename.split('_')[0])
        hwlabels.append(filelabel)
        TrainMatrix[i, :] = img2vector('trainingDigits/%s' %file)

    hwTestfiles = os.listdir('./testDigits')
    hwTestNum = len(hwTestfiles)
    errornums = 0.0

    for j in range(hwTestNum):
        file = hwTestfiles[j]
        filename = file.split('.')[0]
        fileTestLabel = int(filename.split('_')[0])
        TestMat = img2vector('testDigits/%s'%file)
        resultLabel = classify0(TestMat, TrainMatrix, hwlabels, 3)

        print "the %d the test result is %d, the real label should be %d"\
              %(j, resultLabel, fileTestLabel)

        if (resultLabel != fileTestLabel):
            errornums += 1

    errorrate = errornums/float(hwTestNum)

    print "the result is : error num is %d, the error rate is %f "\
          %(errornums, errorrate)

    return errorrate
























