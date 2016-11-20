__author__ = 'CC'
import csv
import math

old_loupan = []
new_loupan = []
count = 0
avg_old = 0

def new():
    new = open('../data/shangpin_gm_result/result_new.csv')
    rows = csv.reader(new)
    for row in rows:
        new_loupan.append(float(row[0]))
        count = count + 1

def old():
    old = open('../data/shangpin_gm_result/result_old.csv')
    rows = csv.reader(old)
    sum = 0
    for row in rows:
        old_loupan.append(float(row[0]))
        sum = sum + float(row[0])
    avg_old = float(sum) / count

def mseAndRmse():
    sum = 0
    for key in xrange(count):
        sum = sum + abs((new_loupan[key] - old_loupan[key])*(new_loupan[key] - old_loupan[key]))
    print float(sum)/count, (math.sqrt(sum))/count

def maeAndMape():
    sum = 0
    for key in xrange(count):
        sum = sum + abs(new_loupan[key] - old_loupan[key])

    per = 0
    for key in xrange(count):
        per = per + abs(new_loupan[key] - old_loupan[key])/ float(abs(old_loupan[key]))

    print float(sum)/count, float(per)/count

def RSquare():
    sum_sse = 0
    for key in xrange(count):
        sum_sse = sum_sse + abs((new_loupan[key] - old_loupan[key])*(new_loupan[key] - old_loupan[key]))
    sse = sum_sse

    sum_sst = 0
    for key in xrange(count):
        sum_sst = sum_sst + abs((old_loupan[key] - avg_old)*(old_loupan[key] - avg_old))
    sst = sum_sst

    r = 1 - float(sse)/sst
    print r

def cal_error():
    new()
    old()
    mseAndRmse()
    maeAndMape()
    RSquare()

cal_error()