__author__ = 'CC'

import csv
import os

data_dictionary = {}

def writeByTags(tag, words):
    file_name = tag+".csv"
    file_name = unicode(file_name, "utf8")   # chinese file name will run error
    os.chdir('../data/tags')
    if not data_dictionary.has_key(tag):
        data_dictionary[tag] = True
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

def splitByTag():
    os.mkdir("../data/tags")
    f = open("../data/selectPrice.csv")
    rows = csv.reader(f)
    for row in rows:

        tags = row[18].split(',')
        for tag in tags:
            writeByTags(tag, row)

splitByTag()