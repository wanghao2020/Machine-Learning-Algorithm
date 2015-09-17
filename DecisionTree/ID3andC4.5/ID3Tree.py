__author__ = 'wanghao'

"""
    the function for the ID3 tree implement
"""


from math import log

# create the dataSet b
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']
    ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

# compute the Shannon entropy
def calShannonEnt(dataSet):

    DataSetNums = len(dataSet)
    ClassCount = {}
    for featVec in dataSet:
        if featVec[-1] not in ClassCount.keys():
            ClassCount[featVec[-1]] = 0;
        ClassCount[featVec[-1]] += 1;

    shannonEnt = 0.0
    for key in ClassCount:
        prob = float(ClassCount[key]) / DataSetNums;
        shannonEnt += -prob * log(prob, 2)

    return shannonEnt

# split the data by one feature value
def splitDataSet(dataSet, axis, value):

    retDataSet = []
    for each in dataSet:
        if each[axis] == value:
            returnVec = each[:axis]
            returnVec.extend(each[axis+1:])
            retDataSet.append(returnVec)

    return retDataSet


# chose the best the feature from dataSet to split the data
def chooseBestFeature(dataSet):

    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1

    for i in range(numFeatures):
        oneFeature = [example[i] for example in dataSet]
        uniqueVals = set(oneFeature)
        NewEntropy = 0.0

        for val in uniqueVals:
            retDataSet = splitDataSet(dataSet, i, val)
            NewEntropy += len(retDataSet) / float(len(dataSet)) * calShannonEnt(retDataSet)

        infoGain = baseEntropy - NewEntropy

        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i


    return bestFeature

# define the leaf node by the major class
def majorityCnt(classList):

    import operator

    classCount = {}
    for oneClass in classList:
        if oneClass not in classCount.keys():
            classCount[oneClass] = 0
        classCount[oneClass] += 1

    # sorted to find the max
    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

# create tree
def createTree(dataSet, labels):

    classList = [example[-1] for example in dataSet]

    # all the date is one class
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # no feature
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    bestFeature = chooseBestFeature(dataSet)
    bestFeatureLabel = labels[bestFeature]
    ID3Tree = {bestFeatureLabel: {}}
    del labels[bestFeature]

    featureList = [example[bestFeature] for example in dataSet]
    uniqueVals = set(featureList)

    for val in uniqueVals:
        subLabel = labels[:]    #important the point to prevent the labels changes
        retDataSet = splitDataSet(dataSet, bestFeature, val)
        ID3Tree[bestFeatureLabel][val] = createTree(retDataSet, subLabel)

    return ID3Tree
























































    return treeDict



































