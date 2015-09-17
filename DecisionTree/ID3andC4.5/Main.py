__author__ = 'wanghao'


"""
   Main function for the ID3 for test or run some functions
"""

import ID3Tree

DataSet, Labels = ID3Tree.createDataSet()
shannon = ID3Tree.calShannonEnt(DataSet)
print "The base dataSet shannon Ent is ", shannon
print "---------------------------------------\n"

retDataSet = ID3Tree.splitDataSet(DataSet, 0, 1)
print retDataSet
print "---------------------------------------\n"

bestFeature = ID3Tree.chooseBestFeature(DataSet)
print "The base dataSet choose the best feature is ", Labels[bestFeature]
print "---------------------------------------\n"

classList = []
for oneData in DataSet:
    classList.append(oneData[-1])

majorClass = ID3Tree.majorityCnt(classList)
print "The base dataSet the major Class is ", majorClass
print "---------------------------------------\n"

myTree = ID3Tree.createTree(DataSet, Labels)
print "The final the ID3 Tree is ", myTree
print "---------------------------------------\n"


# test for the one example
print "Labels is ..", Labels
# !!!Notice:the Labels has been changed
DataSet, Labels = ID3Tree.createDataSet()
result = ID3Tree.classifyID3(myTree, Labels, [1, 10])
print "the classify result is ", result
