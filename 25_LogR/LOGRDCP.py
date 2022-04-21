
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 23:04:18 2021

@author: vikas
"""

import math

math.exp(10)

ls= list(range(-16,16))

y=[]
for x in ls:
    y.append((1)/(1+math.exp(-x)))


import matplotlib.pyplot as plt
plt.scatter(ls,y)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#https://www.datacamp.com/community/tutorials/understanding-logistic-regression-python
#data
url='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/pima-indians-diabetes.csv'
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
# load dataset
pima = pd.read_csv(url, header=None, names=col_names)

pima.head()

x = pima[['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']].values
y = pima['label'].values


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.1)

x_train.shape, x_test.shape, y_train.shape, y_test.shape

from sklearn.linear_model import LogisticRegression

model=LogisticRegression()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)


from sklearn.metrics import accuracy_score, precision_score, recall_score


acc = accuracy_score(y_test, y_pred)
acc

pre = precision_score(y_test, y_pred)
pre

rec = recall_score(y_test, y_pred)
rec

x[1]
x_eval = [[ 1.   , 85.   , 66.   , 29.   ,  0.   , 26.6  ,  0.351, 31.  ], [ 1.   , 85.   , 66.   , 29.   ,  0.   , 26.6  ,  0.351, 31.  ]]

model.predict(x_eval)


'''
y_test = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
y_pred = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

y_pred = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
y_test = [0,0,0,0,0,0,0,0,0,0]

acc = accuracy_score(y_test, y_pred)
acc

pre = precision_score(y_test, y_pred)
pre

rec = recall_score(y_test, y_pred)
rec

'''
'''

from sklearn import metrics

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)

TP = cnf_matrix[0,0]
TN =cnf_matrix[1,1]
FP = cnf_matrix[1,0]
FN = cnf_matrix[0,1]

acc = (TP+TN)/(TP+TN+FP+FN)
acc

prec = TP / (TP + FP)
prec

rec = TP / (TP + FN)
rec

'''
from sklearn.metrics import f1_score

f1 = f1_score(y_test, y_pred)
f1


from sklearn.metrics import roc_curve, roc_auc_score

model.predict_proba(x_test)
model.predict(x_test)

y_pred_proba = model.predict_proba(x_test)[::,1]
y_pred_proba
y_pred_proba.shape

fpr, tpr, _ = roc_curve(y_test, y_pred_proba)

fpr 
tpr


'''


[0,0,0,0,1,0,0,0,1,1]


array([0.49316504, 0.12621985, 0.12763509, 0.24043547, 0.6106026 ,
       0.44047468, 0.33875534, 0.07336317, 0.82416793, 0.71123761])

[0, 0, 0, 0, 0, 0, 1, 0, 1, 1]



TP/ (TP+FN) 

2/(2+1)

TN/(TN+FP)
6 / (6 + 1)

fpr 
[0.        , 0.        , 0.        , 0.42857143, 0.42857143,
       1.        ]

tpr
[0.        , 0.33333333, 0.66666667, 0.66666667, 1.        ,
       1.        ]
'''



auc = roc_auc_score(y_test, y_pred_proba)
auc

#together

plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show();



acc
pre
rec
f1
auc
