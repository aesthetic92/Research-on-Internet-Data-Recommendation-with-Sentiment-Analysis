__author__ = 'CC'

import csv
import math

def precess(rows):
    count = 0
    for i in xrange(len(rows)-1):
        count = count + int(rows[i + 1])
    avg = count / (len(rows) - 1)

    mse = 0
    for i in xrange(len(rows)-1):
        mse = mse + (int(rows[i+1])-avg)*(int(rows[i+1])-avg)

    mse = math.sqrt(mse / (len(rows)-1))
    return mse
