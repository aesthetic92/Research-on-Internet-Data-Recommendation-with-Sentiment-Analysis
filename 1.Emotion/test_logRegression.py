__author__ = 'CC'


from numpy import *
from LogRegression import *
import time

def loadData():
    train_x = []
    train_y = []
    count = 0
    fileIn = open('I:\\Code\\Python\\Emotion\\dataset\\0330\\train_32.txt')
    for line in fileIn.readlines():
        count = count + 1
        if(count <= 80):
            lineArr = line.strip().split(",")
            # float(lineArr[0]),float(lineArr[1]), float(lineArr[2]),float(lineArr[3]), float(lineArr[4]),float(lineArr[5]), float(lineArr[6]), float(lineArr[7])
            # train_x.append([1.0,float(lineArr[3]), float(lineArr[4]), float(lineArr[5]), float(lineArr[6])])
            train_x.append([1.0,float(lineArr[3]), float(lineArr[4]),float(lineArr[5]), float(lineArr[6]), float(lineArr[7])])
            train_y.append(float(lineArr[8]))

    return mat(train_x), mat(train_y).transpose()

def loadTestData():
    test_x = []
    test_y = []
    count = 0
    fileIn = open('I:\\Code\\Python\\Emotion\\dataset\\0330\\train_32.txt')
    for line in fileIn.readlines():
        count = count + 1
        if(count > 80):
            lineArr = line.strip().split(",")
            # test_x.append([1.0,float(lineArr[3]), float(lineArr[4]),float(lineArr[5]), float(lineArr[6])])
            test_x.append([1.0,float(lineArr[3]), float(lineArr[4]), float(lineArr[5]), float(lineArr[6]), float(lineArr[7])])
            test_y.append(float(lineArr[8]))
    return mat(test_x), mat(test_y).transpose()


## step 1: load data
print "step 1: load data..."
train_x, train_y = loadData()
test_x, test_y = loadTestData()

## step 2: training...
print "step 2: training..."
opts = {'alpha': 0.01, 'maxIter':500, 'optimizeType': 'gradDescent'}
optimalWeights = trainLogRegres(train_x, train_y, opts)

## step 3: testing
print "step 3: testing..."
accuracy = testLogRegres(optimalWeights, test_x, test_y)

## step 4: show the result
print "step 4: show the result..."
print 'The classify accuracy is: %.3f%%' % (accuracy * 100)