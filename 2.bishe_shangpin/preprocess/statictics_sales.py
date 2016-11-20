__author__ = 'CC'
import csv

data_dictionary = {}

data1 = {}
data2 = {}
data3 = {}
data4 = {}
data5 = {}

def StatisticsItem():
    f = open("../data/2013_2015.12_sale_data.csv")
    rows = csv.reader(f)
    for row in rows:
        if not data_dictionary.has_key(row[0]):
            data_dictionary[row[0]] = True
            data1[row[0]] = 0
            data2[row[0]] = 0
            data3[row[0]] = 0
            data4[row[0]] = 0
            data5[row[0]] = 0

def StatisticsSales():

    f = open("../data/2013_2015.12_sale_data.csv")
    # f = open("../data/test.csv")
    rows = csv.reader(f)
    for row in rows:
        if row in data_dictionary:
            data = []
            data.append(row[5])

    for key in data1:
        w = open("../data/statictics_sale_data.csv", 'ab')
        write = csv.writer(w)
        write.writerow((key, data1[key], data2[key], data3[key], data4[key], data5[key]))
        w.close()


StatisticsSales()
