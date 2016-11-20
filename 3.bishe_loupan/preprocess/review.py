__author__ = 'CC'

import csv

def precess():
    f = open('I:\\Code\\Python\\bishe_loupan\\data\\train_loupan\\train.csv')
    w = open('I:\\Code\\Python\\bishe_loupan\\data\\train_loupan\\train_data3.csv', 'ab')
    rows = csv.reader(f)
    write = csv.writer(w)

    for row in rows:
        value = []
        value.append(str(row[0]))
        for i in xrange(len(row)-1):
            value.append(int(row[i+1]))

        for i in xrange(66-len(row)):
            value.append(1)

        write.writerow(value)


precess()