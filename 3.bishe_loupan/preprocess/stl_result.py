__author__ = 'CC'

import math
import csv

old_result = []
new_result = []
avg_old = 0

emotion = {}

def linefit(x , y):
    N = float(len(x))
    sx,sy,sxx,syy,sxy=0,0,0,0,0
    for i in range(0,int(N)):
        sx  += x[i]
        sy  += y[i]
        sxx += x[i]*x[i]
        syy += y[i]*y[i]
        sxy += x[i]*y[i]
    a = (sy*sx/N -sxy)/( sx*sx/N -sxx)
    b = (sy - a*sx)/N
    # r = abs(sy*sx/N-sxy)/math.sqrt((sxx-sx*sx/N)*(syy-sy*sy/N))
    return a,b

def getEmotion():
    f = open('I:\\Code\\Python\\bishe_loupan\\data\\train_loupan\\emotion.csv')
    rows = csv.reader(f)
    for row in rows:
        emotion[str(row[0])] = int(row[1].split('.')[0])

def stl():
    f = open('I:\\Code\\Python\\bishe_loupan\\data\\train_loupan\\train_data3.csv')
    rows = csv.reader(f)

    for row in rows:
        arr = row[2:8]
        for i in xrange(len(arr)):
            arr[i] = int(arr[i])
        old_result.append(int(row[1]))

        aver = 0.0
        for i in xrange(len(arr)):
            aver = aver + int(arr[i])
        aver = aver / len(arr)
        aver = round(aver, 1)

        aver_arr = []
        for i in xrange(len(arr)-1):
            temp = (int(arr[i]) + int(arr[i+1]))/2.0
            temp = round(temp, 1)
            aver_arr.append(temp)

        ratio = []
        sum_ratio = 0
        for i in xrange(len(arr)-1):
            temp = (int(arr[i+1])+1) / (int(aver_arr[i])+1)
            temp = round(temp, 1)
            sum_ratio = sum_ratio + temp
            ratio.append(temp)

        aver_ratio = []
        for i in xrange(len(ratio)):
            temp = ratio[i] * (len(ratio) / sum_ratio)
            temp = round(temp, 1)
            aver_ratio.append(temp)

        if len(aver_ratio) > 0:
            value = min(arr) * aver_ratio[0]
            new_result.append(value)


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

    print float(sum)/len(old_result), float(per)/len(old_result)-1

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
    stl()
    mseAndRmse()
    maeAndMape()
    # RSquare()

result()