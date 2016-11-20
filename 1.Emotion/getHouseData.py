# coding=utf-8
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')

dates = {}

def init():
    f = open("I:\\Code\\Python\\Emotion\\dataset\\house\\house7Name.txt", 'r')
    for line in f.readlines():

        for i in xrange(29):
            dates[(line, str(i+1))] = 0

    f.close()

def getDatas():

    init()

    f = open("I:\\Code\\Python\\Emotion\\dataset\\house\\house7.csv")
    rows = csv.reader(f)
    for row in rows:
        houseDate = row[2].split('/')
        day = houseDate[2]
        row[0] = row[0].decode('utf8')
        dates[(row[1], day)] = dates[(row[1], day)] + 1

    loupan = open("I:\\Code\\Python\\Emotion\\dataset\\house\\house7Name.txt", 'r')
    w = open("I:\\Code\\Python\\Emotion\\dataset\\house\\dataset.txt", 'w')
    for line in loupan.readlines():
        print line
        for i in xrange(29):
            w.write(dates[(line, str(i+1))])

        w.write('\n')


getDatas()