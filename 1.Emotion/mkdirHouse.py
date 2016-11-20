# coding=utf-8

import csv
import os

data_dictionary = {}


def writeByMusician(musician, words):
    file_name = musician+".txt"
    if not data_dictionary.has_key(musician):
        data_dictionary[musician] = True
        file_name = "I:\\Code\\Python\\Emotion\\dataset\\house7mEmotion\\" + file_name
        f = open(file_name, 'a')
        f.write(words)
        f.close()
    else :
        file_name = "I:\\Code\\Python\\Emotion\\dataset\\house7mEmotion\\" + file_name
        f = open(file_name, 'a')
        f.write(words)
        f.close()

def splitByMusician():
    f = open("I:\\Code\\Python\\Emotion\\dataset\\house\\house7Name.txt", 'r')
    for row in f.readlines():
        print row[0]
        musician = row[0]
        words = row[0]
        writeByMusician(musician, words)

splitByMusician()