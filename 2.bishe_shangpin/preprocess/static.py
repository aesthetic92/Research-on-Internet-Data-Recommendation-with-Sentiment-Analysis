__author__ = 'CC'

import csv

def statictics():
    f = open('I:\\Code\\Python\\bishe_shangpin\\data\\train_shangpin\\train_data.csv')
    rows = csv.reader(f)
    sum = 0
    for row in rows:
        for i in xrange(len(row)-1):
            sum = sum + int(row[i+1])

    print sum

statictics()