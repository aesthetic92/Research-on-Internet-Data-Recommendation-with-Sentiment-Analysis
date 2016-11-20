__author__ = 'CC'

import csv
import math

loupan_name = {}

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

def result():
    f = open("../data/train/train_data.csv")
    rows = csv.reader(f)

    old = {}
    new = {}

    for row in rows:
        arr = row[2:len(row)]

        old[row[0]] = int(row[1])
        new[row[0]] = int(row[1])

        value_new = int(row[1])
        if(len(arr) > 1):
            X = []
            Y = []
            for i in xrange(len(arr)):
                X.append(i+1)
                Y.append(int(arr[len(arr)-i-1]))

            a, b= linefit(X, Y)
            value_new = a * (len(arr)+1) + b
            value_new = round(value_new, 1)
            new[row[0]] = value_new

    old_sort = sorted(old.iteritems(), key=lambda e:e[1], reverse=True)
    new_sort = sorted(new.iteritems(), key=lambda e:e[1], reverse=True)

    w = open("../data/regression_result/result_old.csv", 'ab')
    write_old = csv.writer(w)
    for value in old_sort:
        write_old.writerow((value[0], value[1]))
    w.close()

    w1= open("../data/regression_result/result_new.csv", 'ab')
    write_new = csv.writer(w1)
    for value in new_sort:
        write_new.writerow((value[0], value[1]))
    w1.close()

result()



