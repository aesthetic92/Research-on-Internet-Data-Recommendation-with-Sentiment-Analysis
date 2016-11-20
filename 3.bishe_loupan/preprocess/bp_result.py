#coding=utf-8

import numpy as np
# import matplotlib.pyplot as plt

import math
import csv

old_result = []
new_result = []
avg_old = 0
emotion = {}
index = 2

def getEmotion():
    f = open('I:\\Code\\Python\\bishe_loupan\\data\\train_loupan\\emotion.csv')
    rows = csv.reader(f)
    for row in rows:
        emotion[str(row[0])] = int(row[1].split('.')[0])

def logsig(x):
    return 1/(1+np.exp(-x))

def bp():
    f = open('I:\\Code\\Python\\bishe_loupan\\data\\train_loupan\\train_data3.csv')
    rows = csv.reader(f)
    arr2 = []
    arr3 = []
    arr4 = []
    arr5 = []
    arr6 = []
    arr7 = []
    # score= []
    out_result = []

    #   review
    maxepochs = 500
    errorfinal = 0.65*10**(-3)
    samnum = 344   # review
    indim = 6
    outdim = 1
    hiddenunitnum = 8
    learnrate = 0.004

    for row in rows:
        arr2.append(math.log(int(row[2])+1, index))
        arr3.append(math.log(int(row[3])+1, index))
        arr4.append(math.log(int(row[4])+1, index))
        arr5.append(math.log(int(row[5])+1, index))
        arr6.append(math.log(int(row[6])+1, index))
        arr7.append(math.log(int(row[7])+1, index))
        # score.append(math.log(abs(emotion[str(row[0])])+1, 2))
        old_result.append(int(row[1]))
        out_result.append(math.log(int(row[1])+1, index))

    samplein = np.mat([arr2,arr3,arr4,arr5,arr6,arr7]) #6*100
    sampleinminmax = np.array([samplein.min(axis=1).T.tolist()[0],samplein.max(axis=1).T.tolist()[0]]).transpose()#3*2，对应最大值最小值
    sampleout = np.mat([out_result])#1*100
    sampleoutminmax = np.array([sampleout.min(axis=1).T.tolist()[0],sampleout.max(axis=1).T.tolist()[0]]).transpose()#2*2，对应最大值最小值

    #3*20
    sampleinnorm = (2*(np.array(samplein.T)-sampleinminmax.transpose()[0])/(sampleinminmax.transpose()[1]-sampleinminmax.transpose()[0])-1).transpose()
    #2*20
    sampleoutnorm = (2*(np.array(sampleout.T).astype(float)-sampleoutminmax.transpose()[0])/(sampleoutminmax.transpose()[1]-sampleoutminmax.transpose()[0])-1).transpose()

    #给输出样本添加噪音
    # noise = 0.03*np.random.rand(sampleoutnorm.shape[0],sampleoutnorm.shape[1])
    # sampleoutnorm += noise

    # w1 = 0.5*np.random.rand(hiddenunitnum,indim)-0.1
    # b1 = 0.5*np.random.rand(hiddenunitnum,1)-0.1
    # w2 = 0.5*np.random.rand(outdim,hiddenunitnum)-0.1
    # b2 = 0.5*np.random.rand(outdim,1)-0.1
    w1 = np.zeros((hiddenunitnum,indim))
    b1 = np.zeros((hiddenunitnum,1))
    w2 = np.zeros((outdim,hiddenunitnum))
    b2 = np.zeros((outdim,1))

    errhistory = []

    for i in range(maxepochs):
        hiddenout = logsig((np.dot(w1,sampleinnorm).transpose()+b1.transpose())).transpose()
        networkout = (np.dot(w2,hiddenout).transpose()+b2.transpose()).transpose()
        err = sampleoutnorm - networkout
        sse = sum(sum(err**2))

        errhistory.append(sse)
        if sse < errorfinal:
            break

        delta2 = err

        delta1 = np.dot(w2.transpose(),delta2)*hiddenout*(1-hiddenout)

        dw2 = np.dot(delta2,hiddenout.transpose())
        db2 = np.dot(delta2,np.ones((samnum,1)))

        dw1 = np.dot(delta1,sampleinnorm.transpose())
        db1 = np.dot(delta1,np.ones((samnum,1)))

        w2 += learnrate*dw2
        b2 += learnrate*db2

        w1 += learnrate*dw1
        b1 += learnrate*db1


    # # 仿真输出和实际输出对比图
    hiddenout = logsig((np.dot(w1,sampleinnorm).transpose()+b1.transpose())).transpose()
    networkout = (np.dot(w2,hiddenout).transpose()+b2.transpose()).transpose()
    diff = sampleoutminmax[:,1]-sampleoutminmax[:,0]
    networkout2 = (networkout+1)/2
    networkout2[0] = networkout2[0]*diff[0]+sampleoutminmax[0][0]

    for i in xrange(len(networkout2[0])):
        new_result.append(networkout2[0][i])
    # print new_result

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

    print abs(float(sum)/len(old_result)), abs(float(per)/len(old_result)-1)

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
    # getEmotion()
    bp()
    mseAndRmse()
    maeAndMape()
    # RSquare()

result()