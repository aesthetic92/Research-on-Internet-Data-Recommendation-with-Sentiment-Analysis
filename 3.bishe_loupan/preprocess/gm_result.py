# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import math
import csv

old_result = []
new_result = []
avg_old = 0

emotion = {}
INF = 10000
index = 2

def getEmotion():
    f = open('I:\\Code\\Python\\bishe_loupan\\data\\train_loupan\\emotion.csv')
    rows = csv.reader(f)
    for row in rows:
        emotion[int(row[0])] = int(row[1].split('.')[0])

def readEmotion():
    f = open('I:\\Code\\Python\\bishe_loupan\\data\\train_loupan\\emotion1.csv')
    rows = csv.reader(f)

    for row in rows:
        each_sp = []
        for i in xrange(len(row)-2):
            value = int(row[i+1].split('.')[0])
            each_sp.append(math.log(abs(value)+1, index))
        emotion[str(row[0])] = each_sp

def getTextEmotion(row):
    each_sp = []
    each_sp = emotion[str(row)]

    aver_arr = []
    for i in xrange(len(each_sp)-1):
        temp = (each_sp[i] + each_sp[i+1])/2.0
        temp = round(temp, 1)
        aver_arr.append(temp)

    ratio = []
    sum_ratio = 0
    for i in xrange(len(each_sp)-1):
        temp = (each_sp[i+1]+1) / (aver_arr[i]+1)
        temp = round(temp, 1)
        sum_ratio = sum_ratio + temp
        ratio.append(temp)

    aver_ratio = []
    for i in xrange(len(ratio)):
        temp = ratio[i] * (len(ratio) / sum_ratio)
        temp = round(temp, 1)
        aver_ratio.append(temp)

    result = 1.0
    for i in xrange(len(aver_ratio)):
        if result > aver_ratio[i]:
            result = aver_ratio[i]
    return result

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

    result = 1.0
    print aver_ratio
    for i in xrange(len(aver_ratio)):
        if result > aver_ratio[i]:
            result = aver_ratio[i]
    return result

def gm():
    f = open('I:\\Code\\Python\\bishe_loupan\\data\\train_loupan\\train_data3.csv')
    rows = csv.reader(f)
    count = 0
    for row in rows:
        history_data = []
        old_result.append(int(row[1]))
        data = row[2:7]
        for i in xrange(len(data)):
            # history_data.append(data[len(data)-1-i])
            history_data.append(math.log(int(data[i]), index))
            # history_data.append(int(data[i]))
        for i in xrange(len(history_data)):
            history_data[i] = int(history_data[i])+1

        print history_data
        n = len(history_data)
        X0 = np.array(history_data)

        #累加生成
        history_data_agg = [sum(history_data[0:i+1]) for i in range(n)]
        X1 = np.array(history_data_agg)

        #计算数据矩阵B和数据向量Y
        B = np.zeros([n-1,2])
        Y = np.zeros([n-1,1])
        for i in range(0,n-1):
            B[i][0] = -0.5*(X1[i] + X1[i+1])
            B[i][1] = 1
            Y[i][0] = X0[i+1]

        #计算GM(1,1)微分方程的参数a和u
        #A = np.zeros([2,1])
        A = np.linalg.inv(B.T.dot(B)).dot(B.T).dot(Y)
        a = A[0][0]
        u = A[1][0]

        #建立灰色预测模型
        XX0 = np.zeros(n)
        XX0[0] = X0[0]
        for i in range(1,n):
            XX0[i] = (X0[0] - u/a)*(1-math.exp(a))*math.exp(-a*(i));


        #模型精度的后验差检验
        e = 0      #求残差平均值
        for i in range(0,n):
            e += (X0[i] - XX0[i])
        e /= n

        #求历史数据平均值
        aver = 0;
        for i in range(0,n):
            aver += X0[i]
        aver /= n

        #求历史数据方差
        s12 = 0;
        for i in range(0,n):
            s12 += (X0[i]-aver)**2;
        s12 /= n

        #求残差方差
        s22 = 0;
        for i in range(0,n):
            s22 += ((X0[i] - XX0[i]) - e)**2;
        s22 /= n

        #求后验差比值
        C = s22 / s12

        #求小误差概率
        cout = 0
        for i in range(0,n):
            if abs((X0[i] - XX0[i]) - e) < 0.6754*math.sqrt(abs(s12)):
                cout = cout+1
            else:
                cout = cout
        P = cout / n

        # if (C < 0.35 and P > 0.95):
        #     print C, P
        #     #预测精度为一级
        #     m = 1   #请输入需要预测的年数
        #     #print('往后m各年负荷为：')
        #     f = np.zeros(m)
        #     for i in range(0,m):
        #         f[i] = (X0[0] - u/a)*(1-math.exp(a))*math.exp(-a*(i+n))
        #         print f[i]
        # else:
        #     print('灰色预测法不适用')

        # print C, P

        result = (X0[0] - u/a)*(1-math.exp(a))*math.exp(-a*(n))
        # result = (X0[0] - u/a)*(1-math.exp(a))*math.exp(-a*(n))*getTextEmotion(row[0])*getEcoEmotion()
        if result > 0:
            new_result.append(result)
            count = count + 1
        else:
            new_result.append(int(row[1]))
    return  new_result

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
    readEmotion()
    gm()
    print "************************************"
    mseAndRmse()
    maeAndMape()
    # RSquare()

result()