__author__ = 'CC'


import csv
import os

data_dictionary = {}


def writeByLoupan(item, words):
    file_name = item+".csv"
    file_name = unicode(file_name, "utf8")   # chinese file name will run error
    os.chdir('../data/Emotion/loupan')
    if not data_dictionary.has_key(item):
        data_dictionary[item] = True
        f = open(file_name, 'ab')
        write = csv.writer(f)
        write.writerow(words)
        f.close()
    else :
        f = open(file_name, 'ab')
        write = csv.writer(f)
        write.writerow(words)
        f.close()

    os.chdir('../../preprocess')

def splitByLoupan():
    os.mkdir("../data/Emotion/loupan")
    f = open("../data/2013_2015.12_sale_data.csv")
    rows = csv.reader(f)
    for row in rows:

        item = row[0]
        writeByLoupan(item, row)

splitByLoupan()