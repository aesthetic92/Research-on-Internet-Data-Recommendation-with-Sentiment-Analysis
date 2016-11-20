__author__ = 'CC'

import csv

loupan_name = {}

def getTrain():
    f = open("../data/2013_2015.12_sale_data.csv")
    rows = csv.reader(f)
    for row in rows:
        if not loupan_name.has_key(str(row[0])):
            new = []
            new.append(int(row[5]))
            loupan_name[str(row[0])] = new

        else:
            arr = loupan_name[str(row[0])]
            arr.append(int(row[5]))
            loupan_name[str(row[0])] = arr

    w = open("../data/train_loupan/train_data.csv", 'ab')
    write = csv.writer(w)
    for key, value in loupan_name.items():
        line = []
        for i in xrange(len(value)):
            line.append(value[i])
        write.writerow(line)

getTrain()



