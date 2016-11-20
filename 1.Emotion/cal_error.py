# coding=utf-8

__author__ = 'CC'


import csv

result = {}
result_cnn = {}

def error():
    f1 = open("I:\\Code\\Python\\Emotion\\0330_resultValue_class.csv")
    rows = csv.reader(f1)
    for row in rows:
        if rows.line_num == 1:
            continue
        if(float(str(row[1])) > 0):
            result[str(row[0])] = 1
        else:
            result[str(row[0])] = 0

    f2 = open("I:\\Code\\Python\\Emotion\\0330_result_class.csv")
    rows2 = csv.reader(f2)
    for row in rows2:
        result_cnn[str(row[0])] = int(str(row[1]))

    count = 0
    for key, value in result_cnn.items():
        if(result_cnn[key] == 1):
            count = count + 1

    print "error ratio = %d%%" % (100 - count)


def test():
    f = open("I:\\Code\\Python\\Emotion\\dataset\\house\\house.csv")
    rows = csv.reader(f)
    for row in rows:
        print row[0], row[1], row[2]

test()