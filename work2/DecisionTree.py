# 生成树
from numpy import *
import numpy as np
import pandas as pd
from math import log
import operator

"""
函数说明:计算给定数据集的经验熵(香农熵)

Parameters:
    dataSet - 数据集
Returns:
    shannonEnt - 经验熵(香农熵)

"""
def calcShannonEnt(dataSet):
    numEntires = len(dataSet)                        #返回数据集的行数
    labelCounts = {}                                #保存每个标签(Label)出现次数的字典
    for featVec in dataSet:                            #对每组特征向量进行统计
        currentLabel = featVec[-1]                    #提取标签(Label)信息
        if currentLabel not in labelCounts.keys():    #如果标签(Label)没有放入统计次数的字典,添加进去
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1                #Label计数
    shannonEnt = 0.0                                #经验熵(香农熵)
    for key in labelCounts:                            #计算香农熵
        prob = float(labelCounts[key]) / numEntires    #选择该标签(Label)的概率
        shannonEnt -= prob * log(prob, 2)            #利用公式计算
    return shannonEnt                                #返回经验熵(香农熵)


"""
函数说明:按照给定特征划分数据集

Parameters:
    dataSet - 待划分的数据集
    axis - 划分数据集的特征
    value - 需要返回的特征的值
Returns:

"""
def splitDataSet(dataSet, axis, value):
    retDataSet = []                                        #创建返回的数据集列表
    for featVec in dataSet:                             #遍历数据集,for循环无需单独声明列表内部的每个元素命名（featVec），此featVec即遍历dataSet中的每个元素，用i代替也可
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]                #去掉axis特征
            reducedFeatVec.extend(featVec[axis+1:])     #将符合条件的添加到返回的数据集
            retDataSet.append(reducedFeatVec)
    return retDataSet                                      #返回划分后的数据集


def splitContinuousDataSet(dataSet, axis, value):
    retDataSetG = []
    retDataSetL = []
    for featVec in dataSet:
        if featVec[axis] > value:
            reducedFeatVecG = featVec[:axis]
            reducedFeatVecG.extend(featVec[axis+1:])
            retDataSetG.append(reducedFeatVecG)
        else:
            reducedFeatVecL = featVec[:axis]
            reducedFeatVecL.extend(featVec[axis+1:])
            retDataSetL.append(reducedFeatVecL)
    return retDataSetG, retDataSetL


"""
函数说明:选择最优特征

Parameters:
    dataSet - 数据集
Returns:
    bestFeature - 信息增益最大的(最优)特征的索引值

"""
def chooseBestFeatureToSplit(dataSet, labels):
    numFeatures = len(dataSet[0]) - 1                   #特征数量
    baseEntropy = calcShannonEnt(dataSet)               #计算数据集的香农熵
    bestInfoGain = 0.0                                  #信息增益
    bestFeature = -1                                    #最优特征的索引值
    bestSplitDic={}
    for i in range(numFeatures):                         #遍历所有特征
        #获取dataSet的第i个所有特征
        featList = [example[i] for example in dataSet]
        #判断是否为离散特征
        if not (type(featList[0].__name == 'float' or type(featList[0].__name__ == 'int'))):
            uniqueVals = set(featList)                         #创建set集合{},元素不可重复
            newEntropy = 0.0                                  #经验条件熵
            for value in uniqueVals:                         #计算信息增益
                subDataSet = splitDataSet(dataSet, i, value)         #subDataSet划分后的子集
                prob = len(subDataSet) / float(len(dataSet))           #计算子集的概率
                newEntropy += prob * calcShannonEnt(subDataSet)     #根据公式计算经验条件熵
            infoGain = baseEntropy - newEntropy                     #信息增益
        else:
            # 产生 n-1个候选划分点
            sortfeatList=sorted(featList)
            splitList = []
            for j in range(len(sortfeatList) - 1):
                splitList.append((sortfeatList[j] + sortfeatList[j+1])/2)
            bestSplitEntropy = 10000
            for j in range(len(splitList)):
                value = splitList[j]
                newEntropy = 0.0
                DataSet = splitContinuousDataSet(dataSet, i , value)
                subDataSetG = DataSet[0]
                subDataSetL = DataSet[1]
                probG = len(subDataSetG) / float(len(dataSet))
                newEntropy += probG * calcShannonEnt(subDataSetG)
                probL = len(subDataSetL) / float(len(dataSet))
                newEntropy += probL * calcShannonEnt(subDataSetL)
                if newEntropy < bestSplitEntropy:
                    bestSplitEntropy = newEntropy
                    bestsplit = j
            bestSplitDic[labels[i]] = splitList[bestsplit]
            infoGain = baseEntropy - bestSplitEntropy

        if (infoGain > bestInfoGain):                             #计算信息增益
            bestInfoGain = infoGain                             #更新信息增益，找到最大的信息增益
            bestFeature = i                                     #记录信息增益最大的特征的索引值
    if type(dataSet[0][bestFeature]).__name__ == 'float' or type(dataSet[0][bestFeature]).__name__ == 'int':
        bestSplitValue = bestSplitDic[labels[bestFeature]]
        labels[bestFeature]=labels[bestFeature]+'<='+str(bestSplitValue)
        for i in range(shape(dataSet)[0]):
            if dataSet[i][bestFeature]<=bestSplitValue:
                dataSet[i][bestFeature]=1
            else:
                dataSet[i][bestFeature]=0
    return bestFeature                                             #返回信息增益最大的特征的索引值

"""
函数说明:统计classList中出现此处最多的元素(类标签)

Parameters:
    classList - 类标签列表
Returns:
    sortedClassCount[0][0] - 出现此处最多的元素(类标签)
"""
def majorityCnt(classList):
    classCount = {}
    for vote in classList:                                        #统计classList中每个元素出现的次数
        if vote not in classCount.keys():classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)        #根据字典的值降序排序
    return sortedClassCount[0][0]                                #返回classList中出现次数最多的元素
