__author__ = 'CC'

import csv

def statictics():
    f = open('I:\\Code\\Python\\bishe_loupan\\data\\train_loupan\\train_data.csv')
    rows = csv.reader(f)
    sum = 0
    for row in rows:
        for i in xrange(len(row)):
            sum = sum + int(row[i])

    print sum

statictics()
