# -*- coding: utf-8 -*-

import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np
from sklearn.metrics import roc_curve, auc


df = pd.read_csv("titanic_all_numeric.csv")

df.columns
df.head()
df.dtypes
#df = df.drop(['age_was_missing'], axis=1)



y = df['survived']

y


X = df.drop(['survived'], axis =1)


df.dtypes

X.columns
y

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()

# fit the model with data
logreg.fit(X_train,y_train)

#
y_pred=logreg.predict(X_test)
y_pred
y_test



from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
cnf_matrix

TP = cnf_matrix[0,0]
TN = cnf_matrix[1,1]

FP = cnf_matrix[1,0]
FN=cnf_matrix[0,1]

(TP+TN)/ (TP+TN+FP+FN)

'''
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))



y_test = [1,1,1,1,1,1,1,1,0,0]
y_pred = [1,1,1,1,1,1,1,1,1,1]
y_test = [0,0,0,0,0,0,0,0,0,0]
'''

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


print("Precision:",metrics.precision_score(y_test, y_pred))
print("Recall:",metrics.recall_score(y_test, y_pred))




y_pred_proba = logreg.predict_proba(X_test)[::,1]
y_pred_proba
y_pred_proba.shape


fpr, tpr, _ = metrics.roc_curve(y_test, y_pred_proba)

fpr 
tpr

auc = metrics.roc_auc_score(y_test, y_pred_proba)
auc

#together

plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show();





import math

ls= list(range(-16,16))
ls


y=[]
for x in ls:
    y.append((1)/(1+math.exp(-x)))


y


import matplotlib.pyplot as plt
plt.scatter(ls,y)