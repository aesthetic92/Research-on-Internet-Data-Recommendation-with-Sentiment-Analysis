__author__ = 'CC'


from numpy import *
from MultiRegression import *
import time
import math
import csv

old_result = []
new_result = []
avg_old = 0
INF = 10000
index = 2
alpha = 0.0003
emotion = {}

def getEmotion():
    f = open('I:\\Code\\Python\\bishe_loupan\\data\\train_loupan\\emotion.csv')
    rows = csv.reader(f)
    for row in rows:
        emotion[str(row[0])] = int(row[1].split('.')[0])

def getEcoEmotion():
    f = open('I:\\Code\\Python\\bishe_loupan\\data\\train_loupan\\per.csv')
    rows = csv.reader(f)
    each_ec = []
    for row in rows:
        each_ec.append(float(str(row[1])))

    aver_arr = []
    for i in xrange(len(each_ec)-1):
        temp = (each_ec[i] + each_ec[i+1])/2.0
        temp = round(temp, 1)
        aver_arr.append(temp)

    ratio = []
    sum_ratio = 0
    for i in xrange(len(each_ec)-1):
        temp = (each_ec[i+1]+1) / (aver_arr[i]+1)
        temp = round(temp, 1)
        sum_ratio = sum_ratio + temp
        ratio.append(temp)

    aver_ratio = []
    for i in xrange(len(ratio)):
        temp = ratio[i] * (len(ratio) / sum_ratio)
        temp = round(temp, 1)
        aver_ratio.append(temp)

    result = INF
    for i in xrange(len(aver_ratio)):
        if result > aver_ratio[i]:
            result = aver_ratio[i]
    return result

def loadData():
    getEmotion()
    train_x = []
    train_y = []
    f = open('I:\\Code\\Python\\bishe_loupan\\data\\train_loupan\\train_data3.csv')
    rows = csv.reader(f)
    for row in rows:
        # train_x.append([1.0, math.log(int(row[2])+1, 2), math.log(int(row[3])+1, 2), math.log(int(row[4])+1, 2), math.log(int(row[5])+1, 2), math.log(int(row[6])+1, 2), math.log(int(row[7])+1, 2)])
        # train_x.append([1.0, math.log(int(row[2])+1, index), math.log(int(row[3])+1, index), math.log(int(row[4])+1, index), math.log(int(row[5])+1, index), math.log(int(row[6])+1, index), math.log(int(row[7])+1, index), math.log(abs(emotion[str(row[0])])+1, index), getEcoEmotion() ])
        # train_x.append([1.0, math.log(int(row[4])+1, 2), math.log(abs(emotion[str(row[0])])+1, 2)])
        train_x.append([1.0, math.log(int(row[4])+1, index), math.log(abs(emotion[str(row[0])])+1, index), getEcoEmotion()])
        old_result.append(int(row[1]))
        train_y.append(math.log(int(row[1])+1, index))
    return mat(train_x), mat(train_y).transpose()

def loadTestData():
    test_x = []
    test_y = []
    f = open('I:\\Code\\Python\\bishe_loupan\\data\\train_loupan\\train_data3.csv')
    rows = csv.reader(f)
    for row in rows:
        # test_x.append([1.0, math.log(int(row[2])+1, 2), math.log(int(row[3])+1, 2), math.log(int(row[4])+1, 2), math.log(int(row[5])+1, 2), math.log(int(row[6])+1, 2), math.log(int(row[1])+1, 2)])
        # test_x.append([1.0, math.log(int(row[2])+1, index), math.log(int(row[3])+1, index), math.log(int(row[4])+1, index), math.log(int(row[5])+1, index), math.log(int(row[6])+1, index), math.log(int(row[7])+1, index), math.log(abs(emotion[str(row[0])])+1, index), getEcoEmotion() ])
        test_x.append([1.0, math.log(int(row[4])+1, index), math.log(abs(emotion[str(row[0])])+1, index), getEcoEmotion()])
        # test_x.append([1.0, math.log(int(row[4])+1, 2), math.log(abs(emotion[int(row[0])])+1, 2)])
        test_y.append(math.log(int(row[1])+1, index))
    return mat(test_x), mat(test_y).transpose()


def mseAndRmse():
    sum = 0
    for key in xrange(len(old_result)):
        sum = sum + abs((new_result[key] - old_result[key])*(new_result[key] - old_result[key]))
    print float(sum)/len(old_result), math.sqrt(float(sum)/len(old_result))

def maeAndMape():
    sum = 0
    for key in xrange(len(old_result)):
        sum = sum + abs(new_result[key] - old_result[key])

    per = 0
    for key in xrange(len(old_result)):
        per = per + (abs(new_result[key] - old_result[key])+1)/ float(abs(old_result[key])+1)

    print abs(float(sum)/(len(old_result))+1), abs(float(per)/len(old_result)-1)

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

print "***********"
mseAndRmse()
maeAndMape()
# RSquare()
