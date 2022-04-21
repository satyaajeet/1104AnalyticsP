# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 20:59:11 2022

@author: vikas
"""

import pandas as pd

from pydataset import data

data('')

mt = data('mtcars')

mt

type(mt)


mt.to_csv("mtcars.csv")


import pandas as pd

df = pd.read_csv('mtcars.csv')
df


df.columns
df.head()
df.tail()

df.head(10)
df.tail(3)

df.dtypes

df.shape

df.columns


type(df['mpg'])

s = pd.Series(range(1,11))
s
s1 = pd.Series(['a', 'b', 'c', 'd', 'e'])
s1


ps1 = pd.Series([100, 200, 300, 400, 500], 
                index = [1,4,3,6,7])
ps1

import pandas as pd
ps2 = pd.Series([100, 200, 300, 400, 500], 
                index = ['a', 'b', 'b', 'c', 'b'])


ps2


ps2['b']
ps2.loc['b']



ps2.iloc[0]
ps2.iloc[1]

ps2.index
ps2.values

ps2.loc[['b','c']]



import numpy as np
ps4 = pd.Series(np.random.randint(1, 100, size=10))
ps4


ps4>30

ps4[ps4>30]
ps4[(ps4>30) & (ps4<70)]


import pandas as pd

course = pd.Series(['BTech', 'MTech', 'MBA', 'BBA'])
strength = pd.Series([100, 200, 150, 250])
fees = pd.Series([1,1.5, 1.2, 1.7])

course
strength
fees


dic = {'Course':course, 'Strength':strength, 'Fees':fees}
dic

df = pd.DataFrame(dic)
df

df.to_csv("CD.csv")

df

df.keys()

df.columns

df['Course']
df.Course

df.index

df

df.index = df.Course

df

df.drop(['Course'], axis=1)


df = pd.DataFrame(dic)
df

df.loc[1:3]
df.loc[:2]

df.iloc[1:3]


df.Course =='MBA'

df[(df.Course== 'MBA') | (df.Course== 'BBA')]

df[[False, False, True, True]]



#Missing Data



import pandas as pd
import numpy as np

placed = pd.Series([None,np.nan, 100, None])

df['Placed'] = placed

df.dropna(axis=0)
df.dropna(axis=1)




pd4 = pd.DataFrame([['dhiraj', 50, 'M', 10000, None], [None, None, None, None, None], ['kanika', 28, None, 5000, None], ['tanvi', 20, 'F', None, None], ['poonam',45,'F',None,None],['upen',None,'M',None, None]])
pd4

pd4.dropna()
pd4.dropna(axis=0)
pd4.dropna(axis=1)
pd4

pd4.dropna(axis='rows')
pd4.dropna(axis='columns')

pd4.dropna(axis='rows', how='any')

pd4.dropna(axis='rows', how='all')
pd4.dropna(axis='columns', how='all')

pd4
pd4.dropna(axis='rows', thresh=3)



pd4.fillna(0)
pd4.fillna(10)
pd4[1].fillna(0)


df = pd.read_csv('airline.csv')

df

df.plot()

df.fillna(0).plot()

df.fillna(method='ffill').plot()

df[:15].fillna(method='bfill')


pd4[1].fillna(method='ffill')



dic = {'Course':course, 'Strength':strength, 'Fees':fees}
dic

df = pd.DataFrame(dic)
df


np.sum(pd4.isnull())

df = pd.read_csv('mtcars.csv')

df.columns

df.isnull()
np.sum(df.isnull())

df.notnull()

(df.describe()).loc['count']

df.sum()
df.std()
df.max()
df.min()



x=[[1,2,3],[4,5,6]]
y=[[10,11,12],[13,14,15]]

x
y

np.concatenate([x,y], axis=1)


grades1 = {'subject1': ['A1','B1','A2','A3'],'subject2': ['A2','A1','B2','B3']   }

grades1

df1 = pd.DataFrame(grades1)
df1

grades2 = {'subject3': ['A1','B1','A2','A3'],'subject4': ['A2','A1','B2','B3']}

df2 = pd.DataFrame(grades2)
df2
df1
df2

pd.concat([df1,df2])
pd.concat([df1,df2], axis=1)


#Syntheic Dataset

import pandas as pd
import numpy as np

rno = pd.Series(range(1001, 1011))
rno

'''
name = []
for i in range(1, 11):
    name.append('Student'+str(i))
name
'''

name = ['Student'+str(i) for i in range(1,11)]
name

gl = ['M', 'F']

gender = np.random.choice(a=gl, size=10)

course = np.random.choice(a=['MBA', 'BBA', 'BTech', 'MTech'], size=10)

marks = np.random.randint(0,101, size=10)
marks

stud = pd.DataFrame({'RNO':rno, 'Name':name, 'Gender':gender, 'course':course,'Marks':marks})
stud



#Syntheic Data with 1lk entries

import pandas as pd
import numpy as np

rno = pd.Series(range(1, 100001))
rno

'''
name = []
for i in range(1, 11):
    name.append('Student'+str(i))
name
'''

name = ['Student'+str(i) for i in range(1,100001)]
name

gl = ['M', 'F']

gender = np.random.choice(a=gl, size=100000)

course = np.random.choice(a=['MBA', 'BBA', 'BTech', 'MTech'], size=100000)

marks = np.random.randint(0,101, size=100000)
marks

stud = pd.DataFrame({'RNO':rno, 'Name':name, 'Gender':gender, 'course':course,'Marks':marks})
stud



fees = pd.DataFrame({'course':['MBA', 'BBA', 'BTech', 'MTech'], 
                     'fees':[1.5, 1, 2.5, 2]})


stud
fees

df = pd.merge(stud, fees)

df.to_csv('stud.csv')




# Merge
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
pd6
pd5

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


fees = pd.DataFrame({'course':['BBA','MBA','BTECH', 'MTECH'], 'fees':[100000, 200000, 150000, 220000]})
fees








































































































