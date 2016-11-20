__author__ = 'CC'

import csv

shangpin_name = {}

def getTrain():
    f = open("../data/train_shangpin/train.csv")
    rows = csv.reader(f)
    for row in rows:
        new = []
        for i in xrange(7):
            if(int(row[9+i]) < 0):
                row[9+i] = -int(row[9+i])
            new.append(int(row[9+i]))
        shangpin_name[str(row[0])] = new

    w = open("../data/train_shangpin/train_data.csv", 'ab')
    write = csv.writer(w)
    for key, value in shangpin_name.items():
        line = []
        line.append(key)
        for i in xrange(len(value)):
            line.append(value[i])
        write.writerow(line)

getTrain()



