import pca
import numpy as np
from numpy import *
import matplotlib.pyplot as plt


def is_num(str):
    try:
        if str == 'NaN':
            return False
        float(str)
        return True
    except ValueError:
        return False


datastring = pca.loadDataSet('imports-85.data', ',')
relist = [
    [],
    [],
    ['alfa-romero', 'audi', 'bmw', 'chevrolet', 'dodge', 'honda', 'isuzu', 'jaguar', 'mazda', 'mercedes-benz',
     'mercury', 'mitsubishi', 'nissan', 'peugot', 'plymouth', 'porsche', 'renault', 'saab', 'subaru', 'toyota',
     'volkswagen', 'volvo'],
    ['diesel', 'gas'],
    ['std', 'turbo'],
    ['four', 'two'],
    ['hardtop', 'wagon', 'sedan', 'hatchback', 'convertible'],
    ['4wd', 'fwd', 'rwd'],
    ['front', 'rear'],
    [],
    [],
    [],
    [],
    [],
    ['dohc', 'dohcv', 'l', 'ohc', 'ohcf', 'ohcv', 'rotor'],
    ['', '', 'two', 'three', 'four', 'five', 'six', '', 'eight', '', '', '', 'twelve'],
    [],
    ['1bbl', '2bbl', '4bbl', 'idi', 'mfi', 'mpfi', 'spdi', 'spfi'],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

lenth = len(datastring)
width = len(datastring[0])
sumMat = np.zeros(width)
numMat = np.zeros(width)
# 数据化为数值型并累积平均值
for i in range(lenth):
    for j in range(width):
        if is_num(datastring[i][j]) != True and datastring[i][j] != '?':
            datastring[i][j] = float(relist[j].index(datastring[i][j])) * 10000
            sumMat[j] += datastring[i][j]
            numMat[j] += 1
        elif datastring[i][j] != '?':
            datastring[i][j] = float(datastring[i][j])
            sumMat[j] += datastring[i][j]
            numMat[j] += 1
# 平均值
aveMat = np.true_divide(sumMat, numMat)
# 填补缺项
for i in range(lenth):
    for j in range(width):
        if datastring[i][j] == '?':
            datastring[i][j] = aveMat[j]
print(datastring)
dataMat = mat(datastring)
print(dataMat)

# below is a quick hack copied from pca.pca()
meanVals = mean(dataMat, axis=0)
meanRemoved = dataMat - meanVals  # remove mean
covMat = cov(meanRemoved, rowvar=0)
eigVals, eigVects = linalg.eig(mat(covMat))
eigValInd = argsort(eigVals)  # sort, sort goes smallest to largest
eigValInd = eigValInd[::-1]  # reverse
sortedEigVals = eigVals[eigValInd]
total = sum(sortedEigVals)
varPercentage = sortedEigVals / total * 100

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(1, 21), varPercentage[:20], marker='^')
plt.xlabel('Principal Component Number')
plt.ylabel('Percentage of Variance')
plt.show()
