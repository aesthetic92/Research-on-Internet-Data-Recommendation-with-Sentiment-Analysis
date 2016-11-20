__author__ = 'CC'

import csv

def classify():
    f = open("I:\\Code\\Python\\Emotion\\0330_resultValue_class.csv")
    rows = csv.reader(f)

    w = open("I:\\Code\\Python\\Emotion\\0330_result_class.csv", 'ab')
    write = csv.writer(w)

    for row in rows:
        value = 0
        if(float(str(row[1])) > 0):
            value = 1

        write.writerow((row[0], value))

classify()