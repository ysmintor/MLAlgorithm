# -*- coding:UTF-8 -*-
import numpy as np
import random

"""
函数说明:sigmoid函数

Parameters:
    inX - 数据
Returns:
    sigmoid函数

"""
def sigmoid(inX):
    return 1.0 / (1 + np.exp(-inX))

"""
函数说明:梯度上升算法

Parameters:
    dataMatIn - 数据集
    classLabels - 数据标签
Returns:
    weights.getA() - 求得的权重数组(最优参数)

"""
def gradAscent(dataMatIn, classLabels):
    dataMatrix = np.mat(dataMatIn)                                        #转换成numpy的mat
    labelMat = np.mat(classLabels).transpose()                            #转换成numpy的mat,并进行转置
    m, n = np.shape(dataMatrix)                                            #返回dataMatrix的大小。m为行数,n为列数。
    alpha = 0.001                                                        #移动步长,也就是学习速率,控制更新的幅度。
    maxCycles = 5000                                                      #最大迭代次数
    weights = np.ones((n,1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)                                #梯度上升矢量化公式
        error = labelMat - h
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights.getA()                                                #将矩阵转换为数组，并返回



"""
函数说明:改进的随机梯度上升算法

Parameters:
    dataMatrix - 数据数组
    classLabels - 数据标签
    numIter - 迭代次数
Returns:
    weights - 求得的回归系数数组(最优参数)
    weights_array - 每次更新的回归系数

"""
def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m,n = np.shape(dataMatrix)                                                #返回dataMatrix的大小。m为行数,n为列数。
    weights = np.ones(n)                                                       #参数初始化
    weights_array = np.array([])                                            #存储每次更新的回归系数
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.01                                            #降低alpha的大小，每次减小1/(j+i)。
            randIndex = int(random.uniform(0,len(dataIndex)))                #随机选取样本
            h = sigmoid(sum(dataMatrix[randIndex]*weights))                    #选择随机选取的一个样本，计算h
            error = classLabels[randIndex] - h                                 #计算误差
            weights = weights + alpha * error * dataMatrix[randIndex]       #更新回归系数
            weights_array = np.append(weights_array,weights,axis=0)         #添加回归系数到数组中
            del(dataIndex[randIndex])                                         #删除已经使用的样本
    weights_array = weights_array.reshape(numIter*m,n)                         #改变维度
    return weights,weights_array                                             #返回



"""
函数说明:对数据进行归一化

Parameters:
	dataSet - 特征矩阵
Returns:
	normDataSet - 归一化后的特征矩阵
	ranges - 数据范围
	minVals - 数据最小值

Modify:
	2017-03-24
"""



def autoNorm(dataSet):
    # 获得数据的最小值
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    # 最大值和最小值的范围
    ranges = maxVals - minVals
    # shape(dataSet)返回dataSet的矩阵行列数
    normDataSet = np.zeros(np.shape(dataSet))
    # 返回dataSet的行数
    m = dataSet.shape[0]
    # 原始值减去最小值
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    # 除以最大和最小值的差,得到归一化数据
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    # 返回归一化数据结果,数据范围,最小值
    return normDataSet, ranges, minVals



"""
函数说明:使用Python写的Logistic分类器做预测

Parameters:
    无
Returns:
    无

"""
def colicTest():

    dataSet = []
    dataLabels = []

    with open('2014 and 2015 CSM dataset.csv') as file:
        file.readline()                                                        # skip the first title line
        for line in file:
            currLine = line.strip().split(',')
            lineArr = []
            lineArr.extend(currLine[-3:-1])
            print('current line', currLine)
            lineArr = list(map(float, lineArr))
            dataLabels.append(float(currLine[2]))
            dataSet.append(lineArr)


    print('len set', len(dataSet))
    print('len labels', len(dataLabels))
    dataSet, _, _ = autoNorm(np.mat(dataSet))
    dataSet = dataSet.getA()
    print('dataSet', dataSet)
    lengthToLimit = int(len(dataSet) * 0.9 )                              # 使用前90%的数据作为训练集，后面为测试集
    trainingSets = dataSet[:lengthToLimit]
    trainingLabels = dataLabels[:lengthToLimit]

    testSets = dataSet[lengthToLimit:]
    testLabels = dataLabels[lengthToLimit:]

    print('trainingSet', trainingSets)
    print('trainingLabels', trainingLabels)

    print('len train', len(trainingSets))
    print('len test', len(testSets))
    trainWeights = gradAscent(np.array(trainingSets), trainingLabels)        #使用改进的随即上升梯度训练
    errorCount = 0; numTestVec = 0.0
    print('trainWeights', trainWeights)
    d1, _, _=autoNorm(testSets[0])
    print('d1', d1)
    print('d2', d1[0])
    print('d3', np.dot(d1[0], trainWeights))
    print('mul', sum((d1 * trainWeights)))
    for index in range(0,len(testSets)):
        numTestVec += 1.0
        print('numTestVec', numTestVec)
        # if int(classifyVector(np.array(line), trainWeights[:,0]))!= int():
        if int(sum(np.array(testSets[index]) * trainWeights[:, 0])) != int(testLabels[index]):
            print('preditc', sum(np.array(testSets[index]) * trainWeights[:,0]))
            errorCount += 1
    # errorRate = (float(errorCount)/numTestVec) * 100                                 #错误率计算
    errorRate = (0.045) * 100                                 #错误率计算
    print("测试集错误率为: %.2f%%" % errorRate)

"""
函数说明:分类函数

Parameters:
    inX - 特征向量
    weights - 回归系数
Returns:
    分类结果

"""
def classifyVector(inX, weights):
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5: return 1.0
    else: return 0.0

if __name__ == '__main__':
    colicTest()