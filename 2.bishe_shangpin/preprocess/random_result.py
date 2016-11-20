__author__ = 'CC'

import csv
import math

loupan_name = {}

def result():
    f = open("../data/train/train_data.csv")
    rows = csv.reader(f)

    old = {}
    new = {}

    for row in rows:
        old[row[0]] = int(row[1])
        new[row[0]] = int(row[1])

    old_sort = sorted(old.iteritems(), key=lambda e:e[1], reverse=True)
    new_sort = sorted(new.iteritems(), key=lambda e:e[1], reverse=False)

    w = open("../data/random_result/result_old.csv", 'ab')
    write_old = csv.writer(w)
    for value in old_sort:
        write_old.writerow((value[0], value[1]))
    w.close()

    w1= open("../data/random_result/result_new.csv", 'ab')
    write_new = csv.writer(w1)
    for value in new_sort:
        write_new.writerow((value[0], value[1]))
    w1.close()

result()



