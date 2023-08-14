import numpy as np
import random
import csv


# ------Part 1: 处理数据------
def digitalize(dataSet):
    index = dataSet[1]  # 第二列是连续或离散的依据
    # to transpose the dataSet
    dt1, dictionary = [], [],
    dt2 = [dataSet[0]]
    for j in range(len(dataSet[0])):
        curLine = [x[j] for x in dataSet[2:]]  # 修改3，把1改为2，去掉了第二行
        if (index[j] == '0'):  # 如果是离散变量
            subdictionary = list(set(curLine))
            for num in range(len(subdictionary)):
                curLine = [num + 1 if x == subdictionary[num] else x for x in curLine]
            dictionary.append(subdictionary)
        else:
            dictionary.append([])
        dt1.append(curLine)

    # to transpose the dataSet
    for n in range(len(dt1[0])):
        dt2.append([x[n] for x in dt1])
    return dt2, dictionary


def floatize(dataSet):
    dt = [dataSet[0]]
    for m in range(len(dataSet) - 1):
        a = []
        for n in range(len(dataSet[m + 1])):
            if (dataSet[m + 1][n] == 'NA'):
                a.append(-1.0)
            else:
                a.append(float(dataSet[m + 1][n]))
        dt.append(a)
    return dt


# ------Part 2: 生成回归树------
# 切分数据集为两个子集
def binSplitDataSet(dataSet, feature, value):  # 数据集 待切分特征 特征值
    mat0 = dataSet[np.nonzero(dataSet[:, feature] > value)[0], :]
    mat1 = dataSet[np.nonzero(dataSet[:, feature] <= value)[0], :]
    return mat0, mat1


# Tree结点类型：回归树
def regLeaf(dataSet):  # 生成叶结点，在回归树中是目标变量特征的均值
    return np.mean(dataSet[:, -1])


# 误差计算函数：回归误差
def regErr(dataSet):  # 计算目标的平方误差（均方误差*总样本数）
    return np.var(dataSet[:, -1]) * np.shape(dataSet)[0]


# 二元切分
def chooseBestSplit(indexs, dataSet, leafType=regLeaf, errType=regErr, ops=[0, 10]):
    # 切分特征的参数阈值，用户初始设置好
    tolS = ops[0]  # 允许的误差下降值
    tolN = ops[1]  # 切分的最小样本数

    # 若所有特征值都相同，停止切分
    if len(set(dataSet[1:, -1].T.tolist()[0])) == 1:  # 倒数第一列转化成list 不重复 
        return None, leafType(dataSet)  # 如果剩余特征数为1，停止切分1。
        # 找不到好的切分特征，调用regLeaf直接生成叶结点

    deleteOrNot = True
    if ('time4' in indexs):
        n_values = dataSet[:, indexs.index('time4')].tolist()
        n_values = set([x[0] for x in n_values])
        n_values = list(n_values)
        if (len(n_values) == 1):
            deleteOrNot = False

    n = np.shape(dataSet)[1]
    S = errType(dataSet)  # 最好的特征通过计算平均误差
    bestS = np.inf
    bestIndex = 0
    bestValue = 0
    for featIndex in range(n - 1):  # 遍历数据的每个属性特征
        if (deleteOrNot):
            if (indexs[featIndex] == 'time6'):
                continue
            if (indexs[featIndex] == 'time14'):
                continue
            if (indexs[featIndex] == 'time15'):
                continue

        for splitVal in set((dataSet[:, featIndex].T.A.tolist())[0]):  # 遍历每个特征里不同的特征值
            mat0, mat1 = binSplitDataSet(dataSet, featIndex, splitVal)  # 对每个特征进行二元分类
            if (np.shape(mat0)[0] < tolN) or (np.shape(mat1)[0] < tolN): continue
            newS = errType(mat0) + errType(mat1)
            if newS < bestS:  # 更新为误差最小的特征
                bestIndex = featIndex
                bestValue = splitVal
                bestS = newS

    # 如果切分后误差效果下降不大，则取消切分，直接创建叶结点
    if (S - bestS) < tolS:
        return None, leafType(dataSet)  # 停止切分2
    mat0, mat1 = binSplitDataSet(dataSet, bestIndex, bestValue)

    # 判断切分后子集大小，小于最小允许样本数停止切分3
    if (np.shape(mat0)[0] < tolN) or (np.shape(mat1)[0] < tolN):
        return None, leafType(dataSet)
    return bestIndex, bestValue  # 返回特征编号和用于切分的特征值


# 构建tree
def createTree(index, dataSet, leafType=regLeaf, errType=regErr, ops=[0, 10], m="0"):
    # 数据集默认NumPy Mat 其他可选参数 [结点类型：回归树，误差计算函数，ops包含树构建所需的其他元组]
    feat, val = chooseBestSplit(index, dataSet, leafType, errType, ops)
    if feat == None:
        leaf = {'value': val, 'num': m}
        return leaf  # 满足停止条件时返回叶结点值

    retTree = {}
    # 参数一
    retTree['spInd'] = index[feat]
    # 参数二
    retTree['spVal'] = val
    # 参数三
    retTree['num'] = m

    # 切分后的左右子树
    lSet, rSet = binSplitDataSet(dataSet, feat, val)
    retTree['left'] = createTree(index, lSet, leafType, errType, ops, m + "-1")
    retTree['right'] = createTree(index, rSet, leafType, errType, ops, m + "-2")
    return retTree


# ------Part 3: 读取树------
# 寻找所有的叶子节点
def readLeaves(dataSet, leaves=[]):
    # 先遍历左枝
    if ('value' in dataSet['left']):
        leaves.append(dataSet['left'])  # 如果是叶子，则记录信息
    else:
        readLeaves(dataSet['left'], leaves)  # 否则迭代
    # 再遍历右枝
    if ('value' in dataSet['right']):
        leaves.append(dataSet['right'])
    else:
        readLeaves(dataSet['right'], leaves)
    return (leaves)


# 寻找最优（此处为最大）的叶子节点
def findBestPath(leaves):
    bestVal = 0
    bestPath = ""
    for x in leaves:
        if (x['value'] >= bestVal):
            bestVal = x['value']
            bestPath = x['num']
    return (bestPath)


# 依据叶子节点给予的路径还原分类依据
def bestPath(dataSet, path, header, dictionary, Rules={}):
    R = Rules
    if ('value' not in dataSet):
        rule = header[dataSet['spInd']]  # 将rules替换成对应的名称
        subdictionary = dictionary[dataSet['spInd']]  # 取‘spInd’对应的部分
        if (subdictionary == []):  # 若空
            values = dataSet['spVal']  # 说明没有进行数字化（digitalize）操作
        else:
            leftSet = rightSet = []
            for i in range(len(subdictionary)):
                if (i > dataSet['spVal'] - 1):
                    leftSet.append(subdictionary[i])  # ＞的记在左边
                else:
                    rightSet.append(subdictionary[i])

        if (path[2] == '1'):  # 向左走
            R[rule] = leftSet
            bestPath(dataSet['left'], path[2:], header, dictionary, R)
        else:
            R[rule] = rightSet
            bestPath(dataSet['right'], path[2:], header, dictionary, R)
    return (R)


# ------Part 4:回归预测------
# 分割测试集与训练集
def splitTrain_Valid(dataSet):
    trainSet = validSet = [dataSet[0]]
    for x in dataMat[1:]:
        if (random.sample([1, 2, 3, 4, 5], 1) == 1):
            validSet.append(x)
        else:
            trainSet.append(x)
    return (trainSet, validSet)


def regression(index, dataSet, tree):
    T = tree
    while ('value' not in T):
        j = index.index(T['spInd'])
        if (dataSet[j] > T['spVal']):
            T = T['left']
        else:
            T = T['right']
    return (T['value'])


# 随机抽样生成测试集
def randomSample(dataSet, row, col):
    # dataSet 格式：
    # [[mkt1, mkt2, ..., Eff ],
    # [ 1 ,   2 ,  ..., 0.12],
    #           ... 
    # [ 2,    3 ,  ..., 0.21]]
    rowsIndex = np.random.choice(range(len(dataSet[1:])), row, replace=True)  # 随机重复抽样，抽取row个sample
    colsIndex = np.random.choice(range(len(dataSet[0][1:])), col, replace=False)  # 随机抽取col个参数用以回归

    curLine = [dataSet[0][j] for j in colsIndex]
    curLine.append('Eff')
    Test = [curLine]
    for i in rowsIndex:
        curLine = []
        for j in colsIndex:
            curLine.append(dataSet[i + 1][j])
        curLine.append(dataSet[i + 1][len(dataSet[0]) - 1])
        Test.append(curLine)  # 把EFF补上

    return (Test)


def forestRegression(trainSet, testSet, colNum, leafSample, treeNum):
    residualMat = []
    for i in range(treeNum):
        train = randomSample(trainSet, len(trainSet), colNum)
        Tree = createTree(train[0], np.mat(train[1:]), ops=[0, leafSample])

        residual = []
        for x in testSet[1:]:
            residual.append(x[-1] - regression(testSet[0], x, Tree))
        residualMat.append(residual)
    # 取均值，抵消误差
    residualMat = np.average(np.array(residualMat), axis=0)
    mean, std = np.average(residualMat), np.std(residualMat)
    return (residualMat, mean, std)


# -------主体部分------
# -----------------------------
dataMat, testSet, auction = [], [], []
with open('Attributes-EFF.txt') as fr:
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        dataMat.append(curLine)

with open('testSet.txt') as fr:
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        testSet.append(curLine[1:])
        auction.append(curLine[0])

dataMat, dictionary = digitalize(dataMat)
dataMat = floatize(dataMat)
testSet = digitalize(testSet)[0]
testSet = floatize(testSet)

# ------调参------

with open('Tuning Index.csv', 'w', encoding='utf-8') as file:  # 将结果储存起来
    csv_writer = csv.writer(file)
    for r in range(3):  # 为了降低随机误差，每组参数都跑r轮，取平均值作为结果
        trainSet, validSet = splitTrain_Valid(dataMat)  # 分割测试集与训练集
        curLineMean, curLineStd = [], []
        for parameter in range(30):
            data, mean, std = forestRegression(trainSet, validSet, 15, 1, parameter + 1)
            # 输出
            print("round:", r, " numTree:", parameter + 1, round(mean, 3), round(std, 3))
            curLineMean.append(mean)
            curLineStd.append(std)
        csv_writer.writerow(curLineMean)
        csv_writer.writerow(curLineStd)

# ------得到最优模型
'''trainSet, validSet = splitTrain_Valid(dataMat)
numX,numLeaf = 5,9
forest = []
for numTree in range(25):   #生成森林
    train = randomSample(trainSet, len(trainSet), numX)
    tree = createTree(train[0],np.mat(train[1:]), ops=[0, numLeaf])
    forest.append(tree)
    print(tree)'''

# 回归预测
'''validRes, testRes = []
for x in validSet[1:]:
    predictedEff = 0
    for numTree in range(25):
        predictedEff = predictedEff + regression(validSet[0],x,forest[numTree])'''