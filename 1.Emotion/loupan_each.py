#! /usr/bin/env python2.7
#coding=utf-8

"""
Compute a review's positive and negative score, their average score and standard deviation.
This module aim to extract review positive/negative score, average score and standard deviation features (all 6 features).
Sentiment analysis based on SentimentDictionary.

"""


import numpy as np
import os
import textprocessing as tp


# 1. Load dictionary and dataset
# Load SentimentDictionary
"""


# Load dataset
review = tp.get_excel_data("D:/code/review_set.xlxs", "1", "1", "data")

"""

posdict = tp.get_txt_data("I:\\Code\\Python\\Emotion\\posdict.txt","lines")
negdict = tp.get_txt_data("I:\\Code\\Python\\Emotion\\negdict.txt","lines")

# Load AdverbsOfDegreeDictionary
mostdict = tp.get_txt_data('I:\\Code\\Python\\Emotion\\most.txt', 'lines')
verydict = tp.get_txt_data('I:\\Code\\Python\\Emotion\\very.txt', 'lines')
moredict = tp.get_txt_data('I:\\Code\\Python\\Emotion\\more.txt', 'lines')
ishdict = tp.get_txt_data('I:\\Code\\Python\\Emotion\\ish.txt', 'lines')
insufficientdict = tp.get_txt_data('I:\\Code\\Python\\Emotion\\insufficiently.txt', 'lines')
inversedict = tp.get_txt_data('I:\\Code\\Python\\Emotion\\inverse.txt', 'lines')

# Load dataset
#review = tp.get_excel_data("E:/GraduationProject/pythoncode/project/Prediction/main/ReviewSet/HTC.xlsx", 1, 12, "data")
#review = tp.get_excel_data("E:/GraduationProject/pythoncode/project/Prediction/main/ReviewSet/OPPO.xlsx", 1, 12, "data")
#review = tp.get_excel_data("E:/GraduationProject/pythoncode/project/Prediction/main/ReviewSet/MeiZuMX.xlsx", 1, 12, "data")
#review = tp.get_excel_data("E:/GraduationProject/pythoncode/project/Prediction/main/ReviewSet/Samsung.xlsx", 1, 12, "data")
#review = tp.get_commenttxt_data("I:\\Code\\Python\\Emotion\\comment")
#review = tp.get_txt_data('I:\\Code\\Python\\Emotion\\comment\\112438.txt', 'lines')
#获取excel中第一页的第一列的值
#print review[1]


# 2. Sentiment dictionary analysis basic function
# Function of matching adverbs of degree and set weights
def match(word, sentiment_value):
	if word in mostdict:
		sentiment_value *= 4.0
	elif word in verydict:
	    sentiment_value *= 3.0
	elif word in moredict:
	    sentiment_value *= 2.5
	elif word in ishdict:
	    sentiment_value *= 1.0
	elif word in insufficientdict:
	    sentiment_value *= 0.5
	elif word in inversedict:
	    sentiment_value *= -3.0
	return sentiment_value

# Function of transforming negative score to positive score
# Example: [5, -2] →  [7, 0]; [-4, 8] →  [0, 12]
def transform_to_positive_num(poscount, negcount):
    pos_count = 0
    neg_count = 0
    if poscount < 0 and negcount >= 0:
        neg_count += negcount - poscount
        pos_count = 0
    elif negcount < 0 and poscount >= 0:
        pos_count = poscount - negcount
        neg_count = 0
    elif poscount < 0 and negcount < 0:
        neg_count = -poscount
        pos_count = -negcount
    else:
        pos_count = poscount
        neg_count = negcount
    return [pos_count, neg_count]


# 3.1 Single review's positive and negative score
# Function of calculating review's every sentence sentiment score
def sumup_sentence_sentiment_score(score_list):
	score_array = np.array(score_list) # Change list to a numpy array
	Pos = np.sum(score_array[:,0]) # Compute positive score
	Neg = np.sum(score_array[:,1])
	AvgPos = np.mean(score_array[:,0]) # Compute review positive average score, average score = score/sentence number
	AvgNeg = np.mean(score_array[:,1])
	StdPos = np.std(score_array[:,0]) # Compute review positive standard deviation score
	StdNeg = np.std(score_array[:,1])

	return [Pos, Neg, AvgPos, AvgNeg, StdPos, StdNeg]

def single_review_sentiment_score(review):
	single_review_senti_score = []
	cuted_review = tp.cut_sentence_2(review)

	for sent in cuted_review:
		seg_sent = tp.segmentation(sent, 'list')
		i = 0 # word position counter
		s = 0 # sentiment word position
		poscount = 0 # count a positive word
		negcount = 0 # count a negative word

		for word in seg_sent:
		    if word in posdict:
		        poscount += 1
		        for w in seg_sent[s:i]:
		           poscount = match(w, poscount)
		        a = i + 1

		    elif word in negdict:
		        negcount += 1
		        for w in seg_sent[s:i]:
		        	negcount = match(w, negcount)
		        a = i + 1

		    # Match "!" in the review, every "!" has a weight of +2
		    elif word == "！".decode('utf8') or word == "!".decode('utf8'):
		        for w2 in seg_sent[::-1]:
		            if w2 in posdict:
		            	poscount += 2
		            	break
		            elif w2 in negdict:
		                negcount += 2
		                break                    
		    i += 1

		single_review_senti_score.append(transform_to_positive_num(poscount, negcount))
		review_sentiment_score = sumup_sentence_sentiment_score(single_review_senti_score)

	return review_sentiment_score

# Testing
"""
print single_review_sentiment_score(review[0])
"""

# for i in xrange(10):
#     print review[i]
#     print single_review_sentiment_score(review[i])



# 3.2 All review dataset's sentiment score
def sentence_sentiment_score(dataset):
    cuted_review = []
    for cell in dataset:
        cuted_review.append(tp.cut_sentence_2(cell))

    single_review_count = []
    all_review_count = []
    for review in cuted_review:
        for sent in review:
            seg_sent = tp.segmentation(sent, 'list')
            i = 0 #word position counter
            a = 0 #sentiment word position
            poscount = 0 #count a pos word
            negcount = 0
            for word in seg_sent:
                if word in posdict:
                    poscount += 1                
                    for w in seg_sent[a:i]:
                       poscount = match(w, poscount)
                    a = i + 1

                elif word in negdict:
                    negcount += 1
                    for w in seg_sent[a:i]:
                    	negcount = match(w, negcount)
                    a = i + 1

                elif word == '！'.decode('utf8') or word == '!'.decode('utf8'):
                    for w2 in seg_sent[::-1]:
                        if w2 in posdict:
                        	poscount += 2
                        	break
                        elif w2 in negdict:
                            negcount += 2
                            break                    
                i += 1
                
            single_review_count.append(transform_to_positive_num(poscount, negcount)) #[[s1_score], [s2_score], ...]
        all_review_count.append(single_review_count) # [[[s11_score], [s12_score], ...], [[s21_score], [s22_score], ...], ...]
        single_review_count = []    

    return all_review_count

# Compute a single review's sentiment score
def all_review_sentiment_score(senti_score_list):
    score = []
    for review in senti_score_list:
        score_array = np.array(review)
        print "***************"
        print score_array
        print "***************"
        if len(score_array) > 0:
            Pos = np.sum(score_array[:, 0])
            Neg = np.sum(score_array[:,1])
            AvgPos = np.mean(score_array[:,0])
            AvgNeg = np.mean(score_array[:,1])
            StdPos = np.std(score_array[:,0])
            StdNeg = np.std(score_array[:,1])
            score.append([Pos, Neg, AvgPos, AvgNeg, StdPos, StdNeg])
    return score

# Testing
"""
for i in all_review_sentiment_score(sentence_sentiment_score(review)):
	print i
"""

#for i in all_review_sentiment_score(sentence_sentiment_score(review)):
#    print i

#4. Store SentimentDictionary features
resultValue = []
def store_sentiment_dictionary_score(review_set, storepath):
    sentiment_score = all_review_sentiment_score(sentence_sentiment_score(review_set))
    pos = 0
    neg = 0
    f = open(storepath,'w')
    value = []
    for i in sentiment_score:
        pos = pos + i[0]
        neg = neg + i[1]
        f.write(str(i[0])+'\t'+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3])+'\t'+str(i[4])+'\t'+str(i[5])+'\n')
        value.append(i[0]-i[1])
    value.append(pos - neg)
    resultValue.append(value)

    f.write(str(pos) + '\t' + str(neg))
    f.close()



def result():
    path = "I:\\Code\\Python\\Emotion\\1020_loupan_comment"
    filelist = os.listdir(path)
    file_name = []
    for files in filelist:
        Olddir = os.path.join(path,files)
        if(os.path.isdir(Olddir)):
            continue
        filename = os.path.splitext(files)[0]
        readStr = 'I:\\Code\\Python\\Emotion\\1020_loupan_comment\\'+ filename +'.txt'
        writeStr = 'I:\\Code\\Python\\Emotion\\1020_loupan_result_each\\'+ filename +'.txt'
        file_name.append(filename)
        review = tp.get_txt_data(readStr, 'lines')
        store_sentiment_dictionary_score(review,writeStr)
    resultFile = open("I:\\Code\\Python\\Emotion\\1020_loupan_total_emotion.txt", 'w')
    for i in range(len(resultValue)):
        resultFile.write(str(file_name[i]))
        for j in xrange(len(resultValue[i])):
            resultFile.write(','+str(resultValue[i][j]))
        resultFile.write('\n')
    resultFile.close()



result()