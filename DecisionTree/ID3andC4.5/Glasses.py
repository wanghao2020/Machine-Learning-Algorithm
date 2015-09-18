__author__ = 'wanghao'


"""
    the glasses examples
"""

import ID3Tree
import TreePlot

fr = open('./lenses.txt')
DataList = fr.readlines()

DataSet = []
for data in DataList:
    DataSet.append(data.strip().split('\t'))

print "The dateSet is ", DataSet
Labels = ['age', 'prescript', 'astigmatic', 'tearRate']

LenseTree = ID3Tree.createTree(DataSet, Labels)
print "the result ID3 Tree is ", LenseTree

TreePlot.createPlot(LenseTree)
