# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:06:07 2022

@author: vikas
"""

import pandas as pd
import numpy as np
rollno = pd.Series(range(1,11))
name = pd.Series(["student" + str(i) for i in range(1,11)])
genderlist  = ['M','F']
gender = np.random.choice(a=genderlist, size=10, p=[.2,.8])
marks1 = np.random.randint(40,100,size=10)
pd5 = pd.DataFrame({'rollno':rollno, 'name':name, 'gender':gender, 'marks1':marks1})
pd5
rollno = pd.Series(range(6,16))
course = np.random.choice(a=['BBA','MBA','BTECH'], size=10)
marks2 = np.random.randint(40,100,size=10)
pd6 = pd.DataFrame({'rollno':rollno, 'course':course, 'marks2':marks2})
pd5
pd6

pd7 = pd.merge(pd5, pd6)
pd7

pd7 = pd.merge(pd5, pd6, how='inner')
pd7

pd8 = pd.merge(pd5, pd6, how='outer')
pd8

pd9 = pd.merge(pd5, pd6, how='left')
pd9

pd10 = pd.merge(pd5, pd6, how='right')
pd10


fees = pd.DataFrame({'course1':['BBA','MBA','BTECH', 'MTECH'], 'fees':[100000, 200000, 150000, 220000]})
fees

pd8 = pd.merge(pd5, pd6)
pd8


pd11 = pd.merge(pd8, fees, how='outer', left_on = 'course', right_on = 'course1' )
pd11




#groupby


import pandas as pd
import numpy as np

rno = pd.Series(range(1, 100001))
name = ['Student'+str(i) for i in range(1,100001)]
gl = ['M', 'F']
gender = np.random.choice(a=gl, size=100000)
course = np.random.choice(a=['MBA', 'BBA', 'BTech', 'MTech'], size=100000)
marks1 = np.random.randint(0,101, size=100000)
marks2 = np.random.randint(0,101, size=100000)
region = np.random.choice(a=['North', 'South', 'East', 'West'], size=100000)
stud = pd.DataFrame({'RNO':rno, 'Name':name, 'Gender':gender, 'course':course,'Region':region, 'MathMarks':marks2, 'ScienceMarks': marks2})


fees = pd.DataFrame({'course':['MBA', 'BBA', 'BTech', 'MTech'], 
                     'fees':[1.5, 1, 2.5, 2]})


df = pd.merge(stud, fees)

df.head(1)


df.groupby(['Region']).sum()
df.groupby(['Region']).mean()
df.groupby(['Region']).std()


df[['Region', 'course', 'Gender', 'fees']].groupby(['Region', 'course', 'Gender']).sum()


import numpy as np
res = df[['Region', 'course', 'Gender', 'fees']].groupby(['Region', 'course', 'Gender']).aggregate({'fees': [np.sum, np.mean, min, max, np.std]})
res.to_csv('result.csv')

res = df[['Region', 'course', 'Gender', 'fees', 'MathMarks', 'ScienceMarks']].groupby(['Region', 'course', 'Gender']).aggregate({'fees': [np.sum, np.mean, min, max, np.std],
                                                                                                    'MathMarks': [np.sum, np.mean, min, max, np.std],
                                                                                                    'ScienceMarks': [np.sum, np.mean, min, max, np.std]})
res.to_csv('result.csv')





#Case Study

import pandas as pd

df = pd.read_csv('20denco.csv')

df.columns

df.describe()

df.dtypes

df['partnum'] = df['partnum'].astype('object')
df.dtypes

# Loyal customers
df[['custname']].groupby(['custname']).size()
df[['custname']].groupby(['custname']).size().sort_values(ascending=False)
df[['custname']].groupby(['custname']).size().sort_values(ascending=False).head(10)

# Most Selling part Numbers

df[['partnum']].groupby(['partnum']).size()
df[['partnum']].groupby(['partnum']).size().sort_values(ascending=False).head(10)

#Most revenue customers
df[['custname', 'revenue']].groupby(['custname'])['revenue'].sum()
df[['custname', 'revenue']].groupby(['custname'])['revenue'].sum().sort_values(ascending=False).head(10)


#Most revenue Products
df[['partnum', 'revenue']].groupby(['partnum'])['revenue'].sum().sort_values(ascending=False).head(10)

df[['partnum', 'margin']].groupby(['partnum'])['margin'].sum().sort_values(ascending=False).head(10)


#Case Study: RFM Analysis

import pandas as pd

df = pd.read_csv('OnlineRetail.csv', parse_dates =['InvoiceDate'],  encoding= 'unicode_escape')
df.dtypes

df = df.dropna()
df.describe()

df.head()

df['Country'].value_counts()
df['Country'].value_counts().plot(kind='bar')


df = df[df['Country']=='United Kingdom']
df

df = df[df['Quantity']>0]
df


df = df.drop_duplicates()


df['Amount'] = df['Quantity'] * df['UnitPrice']

df.columns

df = df.drop(['StockCode', 'Description', 'Quantity','UnitPrice','Country'], axis=1)

import datetime as dt

PRESENT = dt.datetime(2011,12,10)


df.columns

rfm = df.groupby('CustomerID').agg({'InvoiceDate': lambda date: (PRESENT - date.max()).days,
                              'InvoiceNo': lambda num: len(num),
                              'Amount': lambda price: price.sum()})

rfm
rfm.columns= ['recency','frequency','monetary']
rfm

rfm['r_quartile'] = pd.qcut(rfm['recency'], 3, ['1','2','3'])
rfm['f_quartile'] = pd.qcut(rfm['frequency'], 3, ['3','2','1'])
rfm['m_quartile'] = pd.qcut(rfm['monetary'], 3, ['3','2','1'])

rfm


rfm['RFM_Score'] = rfm.r_quartile.astype(str) + rfm.f_quartile.astype(str) + rfm.m_quartile.astype(str)


rfm[rfm['RFM_Score']=='331'].sort_values(ascending=False, by='monetary').head(10)


rfm[rfm['RFM_Score']=='311'].sort_values(ascending=False, by='monetary').head(10)

rfm[rfm['RFM_Score']=='311'].head(10)





























































