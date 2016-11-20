#! /usr/bin/env python2.7
#coding=utf-8

""" 
Read data from excel file and txt file.
Chinese word segmentation, postagger, sentence cutting and stopwords filtering function.

"""

import jieba
import jieba.posseg
jieba.load_userdict('I:\\Code\\Python\\Emotion\\userdict.txt')
#jieba.load_userdict('E:/Python27/Lib/site-packages/jieba-0.31/jieba/userdict.txt') #Load user dictionary to increse segmentation accuracy

"""
input:
    parameter_1: A txt file with many lines
    parameter_2: A txt file with only one line of data
output:
    parameter_1: Every line is a value of the txt_data list. (unicode)
    parameter_2: Txt data is a string. (str)
"""

def get_txt_data(filepath, para):
    if para == 'lines':
        txt_file1 = open(filepath, 'r')
        txt_tmp1 = txt_file1.readlines()
        txt_tmp2 = ''.join(txt_tmp1)
        txt_data1 = txt_tmp2.decode('utf8').split('\n')
        txt_file1.close()
        return txt_data1
    elif para == 'line':
        txt_file2 = open(filepath, 'r')
        txt_tmp = txt_file2.readline()
        txt_data2 = txt_tmp.decode('utf8')
        txt_file2.close()
        return txt_data2


"""

"""

def segmentation(sentence, para):
    if para == 'str':
        seg_list = jieba.cut(sentence)
        seg_result = ' '.join(seg_list)
        return seg_result
    elif para == 'list':
        seg_list2 = jieba.cut(sentence)
        seg_result2 = []
        for w in seg_list2:
            seg_result2.append(w)
        return seg_result2


"""

"""

def postagger(sentence, para):
    if para == 'list':
        pos_data1 = jieba.posseg.cut(sentence)
        pos_list = []
        for w in pos_data1:
             pos_list.append((w.word, w.flag)) #make every word and tag as a tuple and add them to a list
        return pos_list
    elif para == 'str':
        pos_data2 = jieba.posseg.cut(sentence)
        pos_list2 = []
        for w2 in pos_data2:
            pos_list2.extend([w2.word.encode('utf8'), w2.flag])
        pos_str = ' '.join(pos_list2)
        return pos_str


"""

"""

""" Maybe this algorithm will have bugs in it """
def cut_sentences_1(words):
    #words = (words).decode('utf8')
    start = 0
    i = 0 #i is the position of words
    sents = []
    punt_list = ',.!?:;~，。！？：；～ '.decode('utf8') # Sentence cutting punctuations
    for word in words:
        if word in punt_list and token not in punt_list:
            sents.append(words[start:i+1])
            start = i+1
            i += 1
        else:
            i += 1
            token = list(words[start:i+2]).pop()
    # if there is no punctuations in the end of a sentence, it can still be cutted
    if start < len(words):
        sents.append(words[start:])
    return sents

""" Sentence cutting algorithm without bug, but a little difficult to explain why"""
def cut_sentence_2(words):
    #words = (words).decode('utf8')
    start = 0
    i = 0 #i is the position of words
    token = 'meaningless'
    sents = []
    punt_list = ',.!?;~，。！？；～… '.decode('utf8')
    for word in words:
        if word not in punt_list:
            i += 1
            token = list(words[start:i+2]).pop()
            #print token
        elif word in punt_list and token in punt_list:
            i += 1
            token = list(words[start:i+2]).pop()
        else:
            sents.append(words[start:i+1])
            start = i+1
            i += 1
    if start < len(words):
        sents.append(words[start:])
    return sents


"""
input: An excel file with product reviews
  
output: A multidimentional list of reviews

"""
 
def seg_fil_excel(filepath, sheetnum, colnum):
    # Read product review data from excel file and segment every review
    review_data = []
    for cell in get_excel_data(filepath, sheetnum, colnum, 'data')[0:get_excel_data(filepath, sheetnum, colnum, 'rownum')]:
        review_data.append(segmentation(cell, 'list')) # Seg every reivew
    
    # Read txt file contain stopwords

    stopwords = get_txt_data('I:\\Code\\Python\\Emotion\\stopword.txt','lines')
    # Filter stopwords from reviews
    seg_fil_result = []
    for review in review_data:
        fil = [word for word in review if word not in stopwords and word != ' ']
        seg_fil_result.append(fil)
        fil = []
 
    # Return filtered segment reviews
    return seg_fil_result


"""
input: An excel file with product reviews
  
  
output: A multidimentional list of reviews, use different stopword list, so it will remain sentiment tokens.

"""

def seg_fil_senti_excel(filepath, sheetnum, colnum):
    # Read product review data from excel file and segment every review
    review_data = []
    for cell in get_excel_data(filepath, sheetnum, colnum, 'data')[0:get_excel_data(filepath, sheetnum, colnum, 'rownum')]:
        review_data.append(segmentation(cell, 'list')) # Seg every reivew
    
    # Read txt file contain sentiment stopwords

    sentiment_stopwords = get_txt_data('I:\\Code\\Python\\Emotion\\sentiment_stopword.txt','lines')
    # Filter stopwords from reviews
    seg_fil_senti_result = []
    for review in review_data:
        fil = [word for word in review if word not in sentiment_stopwords and word != ' ']
        seg_fil_senti_result.append(fil)
        fil = []
 
    # Return filtered segment reviews
    return seg_fil_senti_result