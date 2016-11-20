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
    r = abs(sy*sx/N-sxy)/math.sqrt((sxx-sx*sx/N)*(syy-sy*sy/N))
    return a,b,r


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

    w = open("../data/result/result_old.csv", 'ab')
    write_old = csv.writer(w)
    for value in old_sort:
        write_old.writerow((value[0], value[1]))
    w.close()

    w1= open("../data/result/result_new.csv", 'ab')
    write_new = csv.writer(w1)
    for value in new_sort:
        write_new.writerow((value[0], value[1]))
    w1.close()

result()

import csv
import math

musicians = {}
dates = {}

days = {}
artist_start = {}

def result():

    dates_sort = sorted(dates.iteritems(), key=lambda e:e[0], reverse=False)

    for musician in musicians:
        for date in dates_sort:
            days[(musician, date[0])] = 0.0

    for musician in musicians:
        for date in dates_sort:
            artist_start[(musician, date[0])] = 0.0


    for row in rows:
        X = []
        Y = []
        for i in xrange(122):
            X.append(i+1)
            Y.append(int(row[i+1]))
        fit_a, fit_b, fit_r = linefit(X, Y)
        fit_aa = round(fit_a, 1)
        fit_bb = round(fit_b, 1)
        fit_rr = round(fit_r, 1)
        print "--------fit_rr---------"
        print fit_rr

        for i in xrange(31):
            value = fit_aa * (i+1+122) + fit_bb
            if(i < 9):
                artist_start[(row[0], "2015070" + str(i+1))] = value
                artist_start[(row[0], "2015080" + str(i+1))] = value
            elif i == 30:
                 artist_start[(row[0], "201507" + str(i+1))] = value
            else:
                artist_start[(row[0], "201507" + str(i+1))] = value
                artist_start[(row[0], "201508" + str(i+1))] = value

        arr_days = []
        aver_days = []
        aver_ratio = []
        for i in xrange(122):
           arr_days.append(int(row[i+1]))

        for y in xrange(len(arr_days)-6):
            temp = (arr_days[y] + arr_days[y+1] + arr_days[y+2] + arr_days[y+3] + arr_days[y+4] + arr_days[y+5] + arr_days[y+6])/7.0
            temp = round(temp, 1)
            aver_days.append(temp)

        for z in xrange(len(aver_days)):
            temp = arr_days[z+3]/aver_days[z]
            temp = round(temp, 1)
            aver_ratio.append(temp)

        a1 = []
        a2 = []
        a3 = []
        a4 = []
        a5 = []
        a6 = []
        a7 = []
        for k in xrange(len(aver_ratio)):
            if k % 7 == 0:
                a3.append(aver_ratio[k])
            if k % 7 == 1:
                a4.append(aver_ratio[k])
            if k % 7 == 2:
                a5.append(aver_ratio[k])
            if k % 7 == 3:
                a6.append(aver_ratio[k])
            if k % 7 == 4:
                a7.append(aver_ratio[k])
            if k % 7 == 5:
                a1.append(aver_ratio[k])
            if k % 7 == 6:
                a2.append(aver_ratio[k])

        aver_a1 = sum(a1)/len(a1)
        aver_a1 = round(aver_a1, 1)

        aver_a2 = sum(a2)/len(a2)
        aver_a2 = round(aver_a2, 1)

        aver_a3 = sum(a3)/len(a3)
        aver_a3 = round(aver_a3, 1)

        aver_a4 = sum(a4)/len(a4)
        aver_a4 = round(aver_a4, 1)

        aver_a5 = sum(a5)/len(a5)
        aver_a5 = round(aver_a5, 1)

        aver_a6 = sum(a6)/len(a6)
        aver_a6 = round(aver_a6, 1)

        aver_a7 = sum(a7)/len(a7)
        aver_a7 = round(aver_a7, 1)
        print aver_a1, aver_a2, aver_a3, aver_a4, aver_a5, aver_a6, aver_a7

        diff = ((aver_a1 + aver_a2 + aver_a3 + aver_a4 + aver_a5 + aver_a6 + aver_a7) - 7.0)/7.0
        seven = round(diff, 1)

        new_aver_a1 = aver_a1 - diff
        new_aver_a2 = aver_a2 - diff
        new_aver_a3 = aver_a3 - diff
        new_aver_a4 = aver_a4 - diff
        new_aver_a5 = aver_a5 - diff
        new_aver_a6 = aver_a6 - diff
        new_aver_a7 = aver_a7 - diff
        print new_aver_a1, new_aver_a2, new_aver_a3, new_aver_a4, new_aver_a5, new_aver_a6
        print "*******************************"

        date_day = 0
        for date in dates_sort:
            if(date_day%7 == 1):
                days[(row[0], date[0])] = int(artist_start[(row[0], date[0])] * new_aver_a4)

            elif(date_day%7 == 2):
                days[(row[0], date[0])] = int(artist_start[(row[0], date[0])] * new_aver_a5)

            elif(date_day%7 == 3):
                days[(row[0], date[0])] = int(artist_start[(row[0], date[0])] * new_aver_a6)

            elif(date_day%7 == 4):
                days[(row[0], date[0])] = int(artist_start[(row[0], date[0])] * new_aver_a7)

            elif(date_day%7 == 5):
                days[(row[0], date[0])] = int(artist_start[(row[0], date[0])] * new_aver_a1)

            elif(date_day%7 == 6):
                days[(row[0], date[0])] = int(artist_start[(row[0], date[0])] * new_aver_a2)

            elif(date_day%7 == 0):
                days[(row[0], date[0])] = int(artist_start[(row[0], date[0])] * new_aver_a3)
            date_day = date_day + 1

            write.writerow((str(row[0]), str(days[(row[0], date[0])]), str(date[0])))


result()
