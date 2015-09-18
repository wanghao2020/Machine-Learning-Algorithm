__author__ = 'wanghao'


"""
    to plot the tree by the matplotlib
"""

import matplotlib.pyplot as plt
import ID3Tree

# define the decision node, leafnode, arrow args _
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

# plot the node and the arrow
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,
                            xycoords='axes fraction',
                            xytext=centerPt,
                            textcoords='axes fraction',
                            va='center', ha='center',
                            bbox=nodeType,
                            arrowprops=arrow_args)




# plot the mid text
def plotMidText(cntrtPt, parentPt, txtString):

    xMid = (parentPt[0] - cntrtPt[0])/2.0 - cntrtPt[0]
    yMid = (parentPt[1] - cntrtPt[1])/2.0 - cntrtPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)

# plot the tree by the Recursive
def plotTree(myTree, parentpt, nodeTxt):

    numLeafs = ID3Tree.getNumLeafs(myTree)
    maxDepth = ID3Tree.getTreeDepth(myTree)
    firstr = myTree.keys()[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW,
              plotTree.yOff)
    # plot the text and the node
    plotMidText(cntrPt, parentpt, nodeTxt)
    plotNode(firstr, cntrPt, parentpt, decisionNode)

    secondDict = myTree[firstr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD

    # plot the tree by Recursive
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == "dict":
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff),
                     cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))

    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD






# plot the tree main function
def createPlot(tree):

    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plotTree.totalW = float(ID3Tree.getNumLeafs(tree))
    plotTree.totalD = float(ID3Tree.getTreeDepth(tree))

    # init
    plotTree.xOff = -0.5 / plotTree.totalW
    plotTree.yOff = 1.0

    plotTree(tree, (0.5, 1.0), '')
    plt.show()


















