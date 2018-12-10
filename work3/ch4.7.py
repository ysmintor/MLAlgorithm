# -*- coding: UTF-8 -*-
import numpy as np
import random
import re
from collections import Counter

"""
函数说明:将切分的实验样本词条整理成不重复的词条列表，也就是词汇表

Parameters:
    dataSet - 整理的样本数据集
Returns:
    vocabSet - 返回不重复的词条列表，也就是词汇表

"""


def createVocabList(dataSet):
    vocabSet = set()  # 创建一个空的不重复列表
    for document in dataSet:
        vocabSet = vocabSet | set(document)  # 取并集
    return list(vocabSet)


"""
函数说明:根据vocabList词汇表，将inputSet向量化，向量的每个元素为1或0

Parameters:
    vocabList - createVocabList返回的列表
    inputSet - 切分的词条列表
Returns:
    returnVec - 文档向量,词集模型

"""


def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)  # 创建一个其中所含元素都为0的向量
    for word in inputSet:  # 遍历每个词条
        if word in vocabList:  # 如果词条存在于词汇表中，则置1
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec  # 返回文档向量


"""
函数说明:根据vocabList词汇表，构建词袋模型

Parameters:
    vocabList - createVocabList返回的列表
    inputSet - 切分的词条列表
Returns:
    returnVec - 文档向量,词袋模型

"""


def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)  # 创建一个其中所含元素都为0的向量
    for word in inputSet:  # 遍历每个词条
        if word in vocabList:  # 如果词条存在于词汇表中，则计数加一
            returnVec[vocabList.index(word)] += 1
    return returnVec  # 返回词袋模型


"""
函数说明:朴素贝叶斯分类器训练函数

Parameters:
    trainMatrix - 训练文档矩阵，即setOfWords2Vec返回的returnVec构成的矩阵
    trainCategory - 训练类别标签向量，即loadDataSet返回的classVec
Returns:
    p0Vect - 非侮辱类的条件概率数组
    p1Vect - 侮辱类的条件概率数组
    pAbusive - 文档属于侮辱类的概率

"""


def trainNB0(trainMatrix, trainCategory):
    numTrainSet = len(trainMatrix)  # 计算集数目
    numFeatures = len(trainMatrix[0])  # 计算每篇文档的词条数
    classType = classList()
    pClass = [0] * len(classType)
    numClassMap = Counter(trainCategory)
    # 计算每个输出类别所占的概率，即P(Ci)
    for i in range(len(classType)):
        pClass[i] = numClassMap.get(classType[i]) / float(numTrainSet)

    # 创建numpy.ones数组,词条出现数初始化为1，拉普拉斯平滑
    p0Num = np.ones(numFeatures)
    p1Num = np.ones(numFeatures)
    p2Num = np.ones(numFeatures)
    p3Num = np.ones(numFeatures)
    p4Num = np.ones(numFeatures)
    p0Denom = 2.0
    p1Denom = 2.0  # 分母初始化为2,拉普拉斯平滑
    p2Denom = 2.0
    p3Denom = 2.0
    p4Denom = 2.0

    for i in range(numTrainSet):
        if trainCategory[i] == classType[0]:  # 统计属于not_recom类的条件概率所需的数据
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
        elif trainCategory[i] == classType[1]:  # 统计属于recommend类的条件概率所需的数据
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        elif trainCategory[i] == classType[2]:
            p2Num += trainMatrix[i]
            p2Denom += sum(trainMatrix[i])
        elif trainCategory[i] == classType[3]:
            p3Num += trainMatrix[i]
            p3Denom += sum(trainMatrix[i])
        elif trainCategory[i] == classType[4]:
            p4Num += trainMatrix[i]
            p4Denom += sum(trainMatrix[i])

    # 取对数，防止下溢出
    p0Vect = np.log(p0Num / p0Denom)
    p1Vect = np.log(p1Num / p1Denom)
    p2Vect = np.log(p2Num / p2Denom)
    p3Vect = np.log(p3Num / p3Denom)
    p4Vect = np.log(p4Num / p4Denom)



    return p0Vect, p1Vect, p2Vect, p3Vect, p4Vect, pClass  # 返回属于侮辱类的条件概率数组，属于非侮辱类的条件概率数组，文档属于侮辱类的概率


"""
函数说明:朴素贝叶斯分类器分类函数

Parameters:
    vec2Classify - 待分类的词条数组
    p0Vec - 非侮辱类的条件概率数组
    p1Vec -侮辱类的条件概率数组
    pClass1 - 文档属于侮辱类的概率
Returns:
    0 - 属于非侮辱类
    1 - 属于侮辱类

"""


def classifyNB(vec2Classify, p0Vec, p1Vec, p2Vec, p3Vec, p4Vec, pClass):
    # todo 这部份应该可以用np来简化
    p0 = sum(vec2Classify * p0Vec) + np.log(pClass[0])
    p1 = sum(vec2Classify * p1Vec) + np.log(pClass[1])  # 对应元素相乘。logA * B = logA + logB，所以这里加上log(pClass1)
    p2 = sum(vec2Classify * p2Vec) + np.log(pClass[2])
    p3 = sum(vec2Classify * p3Vec) + np.log(pClass[3])
    p4 = sum(vec2Classify * p4Vec) + np.log(pClass[4])

    pList = [p0, p1, p2, p3, p4]
    classIndex = pList.index(max(pList))
    # 找出概率最大的并输出该条件下的分类
    return classList()[classIndex]


"""
函数说明:接收一个大字符串并将其解析为字符串列表

Parameters:
    无
Returns:
    无

"""


def textParse(bigString):  # 将字符串转换为字符列表
    listOfTokens = re.split(r'\w+', bigString)  # 将特殊符号作为切分标志进行字符串切分，即非字母、非数字
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]  # 除了单个字母，例如大写的I，其它单词变成小写


"""
函数说明:打开并解析文件，对数据进行分类：1代表不喜欢,2代表魅力一般,3代表极具魅力

Parameters:
	filename - 文件名
Returns:
	returnMat - 特征矩阵
	classLabelVector - 分类Label向量

Modify:
	2018-10-06
为什么要数据归一化和归一化方法
	https://blog.csdn.net/wuxiaosi808/article/details/78059051
"""


def file2matrix(filename):
    # 打开文件,此次应指定编码，
    fr = open(filename, 'r', encoding='utf-8')
    # 读取文件所有内容
    arrayOLines = fr.readlines()
    # 移除最后多余的'\n'
    arrayOLines.pop()

    # 针对有BOM的UTF-8文本，应该去掉BOM，否则后面会引发错误。
    arrayOLines[0] = arrayOLines[0].lstrip('\ufeff')

    # 生成空的特征数组
    featureList = []
    # 返回的分类标签向量
    classLabelVector = []

    for line in arrayOLines:
        # s.strip(rm)，当rm空时,默认删除空白符(包括'\n','\r','\t',' ')
        line = line.strip()
        # 使用s.split(str="",num=string,cout(str))将字符串根据','分隔符进行切片。
        listFromLine = line.split(',')
        # 将数据提取出来并附加一featureList中
        featureList.append(listFromLine[:-1])
        classLabelVector.append(listFromLine[-1])
    return featureList, classLabelVector


"""

Returns:
    特征分类数据
"""
def featureList():
    features = ['usual', 'pretentious', 'great_pret', 'proper', 'less_proper', 'improper', 'critical', 'very_crit',
                'complete', 'completed', 'incomplete', 'foster', '1', '2', '3', 'more', 'convenient', 'less_conv', 'critical',
                'inconv', 'non-prob', 'slightly_prob', 'problematic', 'recommended', 'priority', 'not_recom']
    return features

def classList():
    classList = ['not_recom', 'recommend', 'very_recom', 'priority', 'spec_prior']
    return classList

"""
函数说明:测试朴素贝叶斯分类器

Parameters:
    无
Returns:
    无

"""


def nursyTest():
    # 打开的文件名
    filename = "nursery.data"
    docList, classList = file2matrix(filename)
    vocabList = featureList()           # 创建词汇表，不重复
    trainingSet = list(range(len(docList)))
    testSet = []  # 创建存储训练集的索引值的列表和测试集的索引值的列表
    for i in range(200):  # 从12960个数据中，随机挑选出12910个作为训练集,200个做测试集
        randIndex = int(random.uniform(0, len(trainingSet)))  # 随机选取索索引值
        testSet.append(trainingSet[randIndex])  # 添加测试集的索引值
        del (trainingSet[randIndex])  # 在训练集列表中删除添加到测试集的索引值

    trainMat = []
    trainClasses = []  # 创建训练集矩阵和训练集类别标签系向量
    for index in trainingSet:  # 遍历训练集
        trainMat.append(bagOfWords2VecMN(vocabList, docList[index]))  # 将生成的词袋模型添加到训练矩阵中
        trainClasses.append(classList[index])  # 将类别添加到训练集类别标签系向量中
    p0V, p1V, p2V, p3V, p4V, pClass = trainNB0(np.array(trainMat), np.array(trainClasses))  # 训练朴素贝叶斯模型

    errorCount = 0  # 错误分类计数
    for index in testSet:  # 遍历测试集
        featureVector = bagOfWords2VecMN(vocabList, docList[index])  # 测试集的词袋模型
        if classifyNB(np.array(featureVector), p0V, p1V, p2V, p3V, p4V, pClass) != classList[index]:  # 如果分类错误
            errorCount += 1  # 错误计数加1
            print("预测错误的测试集：", docList[index])
    print('错误率：%.2f%%' % (float(errorCount) / len(testSet) * 100))


if __name__ == '__main__':
    nursyTest()
