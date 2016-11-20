__author__ = 'CC'


from numpy import *
from MultiRegression import *
import time
import math
import csv
from preprocess import *

old_result = []
new_result = []
emotion = {}
avg_old = 0
INF = 10000
index = 10
alpha = 0.0003

def getEmotion():
    f = open('I:\\Code\\Python\\bishe_shangpin\\data\\train_shangpin\\emotion.csv')
    rows = csv.reader(f)
    for row in rows:
        emotion[int(row[0])] = int(row[1].split('.')[0])

def loadData():
    getEmotion()
    train_x = []
    train_y = []
    f = open('I:\\Code\\Python\\bishe_shangpin\\data\\train_shangpin\\train_data.csv')
    rows = csv.reader(f)
    for row in rows:
        if precess(row) < INF:
            # train_x.append([1.0, math.log(int(row[1])+1, 2), math.log(int(row[2])+1, 2), math.log(int(row[3])+1, 2), math.log(int(row[4])+1, 2), math.log(int(row[5])+1, 2), math.log(int(row[6])+1, 2)])
            # train_x.append([1.0, math.log(int(row[1])+1, index), math.log(int(row[2])+1, index), math.log(int(row[3])+1, index), math.log(int(row[4])+1, index), math.log(int(row[5])+1, index), math.log(int(row[6])+1, index), math.log(abs(emotion[int(row[0])])+1, index)])
            # train_x.append([1.0, math.log(int(row[4])+1, index)])
            train_x.append([1.0, math.log(int(row[4])+1, index), math.log(abs(emotion[int(row[0])])+1, index)])
            old_result.append(int(row[7]))
            train_y.append(math.log(int(row[7])+1, index))
    return mat(train_x), mat(train_y).transpose()

def loadTestData():
    test_x = []
    test_y = []
    f = open('I:\\Code\\Python\\bishe_shangpin\\data\\train_shangpin\\train_data.csv')
    rows = csv.reader(f)
    for row in rows:
        if precess(row) < INF:
            # test_x.append([1.0, math.log(int(row[1])+1, 2), math.log(int(row[2])+1, 2), math.log(int(row[3])+1, 2), math.log(int(row[4])+1, 2), math.log(int(row[5])+1, 2), math.log(int(row[6])+1, 2)])
            # test_x.append([1.0, math.log(int(row[1])+1, index), math.log(int(row[2])+1, index), math.log(int(row[3])+1, index), math.log(int(row[4])+1, index), math.log(int(row[5])+1, index), math.log(int(row[6])+1, index), math.log(abs(emotion[int(row[0])])+1, index)])
            # test_x.append([1.0,math.log(int(row[4])+1, 2)])
            test_x.append([1.0, math.log(int(row[4])+1, index), math.log(abs(emotion[int(row[0])])+1, index)])
            test_y.append(math.log(int(row[7])+1, index))
    return mat(test_x), mat(test_y).transpose()


def mseAndRmse():
    sum = 0
    for key in xrange(len(old_result)):
        sum = sum + abs((new_result[key] - old_result[key])*(new_result[key] - old_result[key]))
    print  math.sqrt(float(sum)/len(old_result))

def maeAndMape():
    sum = 0
    for key in xrange(len(old_result)):
        sum = sum + abs(new_result[key] - old_result[key])

    per = 0
    for key in xrange(len(old_result)):
        per = per + (abs(new_result[key] - old_result[key])+1)/ float(abs(old_result[key])+1)

    print float(sum)/(len(old_result)+1), float(per)/len(old_result)-1

def RSquare():
    sum_sse = 0
    for key in xrange(len(old_result)):
        sum_sse = sum_sse + abs((new_result[key] - old_result[key])*(new_result[key] - old_result[key]))
    sse = sum_sse

    old_sum = 0
    for i in xrange(len(old_result)):
        old_sum = old_sum + old_result[i]
    avg_old = old_sum/len(old_result)

    sum_sst = 0
    for key in xrange(len(old_result)):
        sum_sst = sum_sst + abs((old_result[key] - avg_old)*(old_result[key] - avg_old))
    sst = sum_sst

    r = 1 - float(sse)/sst
    print r

def result():
    getEmotion()
    ## step 1: load data
    print "step 1: load data..."
    train_x, train_y = loadData()
    test_x, test_y = loadTestData()

    ## step 2: training...
    print "step 2: training..."
    opts = {'alpha': alpha, 'maxIter':500, 'optimizeType': 'stocGradDescent'}
    optimalWeights = trainLogRegres(train_x, train_y, opts)

    ## step 3: testing
    print "step 3: testing..."
    nums = testLogRegres(optimalWeights, test_x, test_y)
    for i in xrange(len(nums)):
        new_result.append(nums[i])

    print "*********************************"
    mseAndRmse()
    maeAndMape()
    # RSquare()

result()