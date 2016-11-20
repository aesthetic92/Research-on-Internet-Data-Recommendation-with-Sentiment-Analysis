__author__ = 'CC'

import math
import csv

from bpbp_result import *
from bpbp_result_emotion import *
from multi_regression_result import *
from multi_regression_result_emotion import *
from stl_result import *
from stl_result_emotion import *
from gm_result import *
from gm_result_emotion import *


arr1= []
#   review
maxepochs = 1500
errorfinal = 0.65*10**(-3)
samnum = len(arr1)   # review
indim = 7
outdim = 1
hiddenunitnum = 8
learnrate = 0.005
maxIter = 500
alpha = 0.003
optimizeType = 'stocGradDescent'


def getEmotion():
    f = open('I:\\Code\\Python\\bishe_shangpin\\data\\train_shangpin\\emotion.csv')
    rows = csv.reader(f)
    for row in rows:
        emotion[int(row[0])] = int(row[1].split('.')[0])

bp()
gm()
stl()
