# coding=utf-8


import csv
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

data_dictionary = {}

def splitByHouseName():
    f = open("I:\\Code\\Python\\Emotion\\dataset\\house\\house7.csv")
    w = open("I:\\Code\\Python\\Emotion\\dataset\\house\\house7Name.txt", 'a')
    rows = csv.reader(f)
    for row in rows:
        if not data_dictionary.has_key(row[1]):
            data_dictionary[row[1]] = True
            w.write(row[1] + '\n')

splitByHouseName()
