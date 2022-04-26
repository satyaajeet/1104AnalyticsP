# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 20:51:35 2022

@author: vikas
"""


import pandas as pd
df = pd.read_csv("cardetails.csv")
df.iloc[0]['mileage']
df.dtypes
df = df.dropna().reset_index()
df = df.drop(['index'], axis=1)


def removeextrastr(para):
    fl = []
    for i in range(len(df)):
        s=''
        for j in para[i]:
            if ((ord(j)>48 and ord(j)< 57) or ord(j)==46):
                s=s+j
        try:
            fl.append(float(s))
        except:
            fl.append(float(0))
    return(pd.Series(fl))
        
        
df['engine'] = removeextrastr(df['engine'].values)
df['mileage'] = removeextrastr(df['mileage'].values)
df['max_power'] = removeextrastr(df['max_power'].values)

df.dtypes

df = df.drop(['name'], axis=1)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['fuel'] = le.fit_transform(df['fuel'])
le = LabelEncoder()
df['seller_type'] = le.fit_transform(df['seller_type'])
le = LabelEncoder()
df['transmission'] = le.fit_transform(df['transmission'])
le = LabelEncoder()
df['owner'] = le.fit_transform(df['owner'])

df.dtypes


rep = lambda x: x.split('@')[0] if(x.split('@')[0] != '') else '0'
df['torque']= df['torque'].apply(rep)

df['torque'][df['torque']=='']

df['torque'] = removeextrastr(df['torque'].values)
df.to_csv('res.csv')



df.columns

X = df.drop(['selling_price'], axis=1).values
Y = df['selling_price'].values


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,Y)
ypred = model.predict(X)

r2 = model.score(X,Y)
r2

import matplotlib.pyplot as plt
import seaborn as sns


sns.pairplot(df, size=1.8, aspect=1.8,
                  plot_kws=dict(edgecolor="k", linewidth=0.5),
                  diag_kind="kde", diag_kws=dict(shade=True))



df.columns
col = df.drop('selling_price', axis=1).columns

import seaborn as sns
sns.set_theme()
df.columns





for i in col:
    g = sns.lmplot(
        data=df,
        x=i, y="selling_price",
        height=5)








df.columns
X = df.drop(['selling_price', 'se@s', 'engine'], axis=1).values
Y = df['selling_price'].values


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,Y)
ypred = model.predict(X)

r2 = model.score(X,Y)
r2



import pandas as pd
df = pd.read_csv("car1.csv")
df.dtypes
df =df.drop(['name'],axis=1)
df = df.dropna().reset_index()
df = df.drop(['index'], axis=1)
df.dtypes


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['fuel'] = le.fit_transform(df['fuel'])
le = LabelEncoder()
df['seller_type'] = le.fit_transform(df['seller_type'])
le = LabelEncoder()
df['transmission'] = le.fit_transform(df['transmission'])
le = LabelEncoder()
df['owner'] = le.fit_transform(df['owner'])


X = df.drop(['selling_price'], axis=1).values
Y = df['selling_price'].values


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X,Y)
ypred = model.predict(X)

r2 = model.score(X,Y)
r2

import matplotlib.pyplot as plt
import seaborn as sns


sns.pairplot(df, size=1.8, aspect=1.8,
                  plot_kws=dict(edgecolor="k", linewidth=0.5),
                  diag_kind="kde", diag_kws=dict(shade=True))






