# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 20:54:49 2022

@author: vikas
"""

import random as rd

r1 = rd.randint(1,10)
r1

r2 = rd.randrange(0, 100, 3)
r2

rd.ran

l1 = list(range(1,100))
l1

r3 = rd.choices(l1, k=1000)
r3

#Numpy

import numpy as np

r1 = np.random.randint(10)
r1


r2 = np.random.randint(10, 100)
r2

#1 Dim
r3 = np.random.randint(1, 10, size=9)
r3

type(r3)

#Homogeneous

#2 Dim
r4 = np.random.randint(1, 30, size=(3,4))
r4

r4.shape

r4 = r4.reshape(4,3)
r4.shape


r4 = r4.reshape(2,6)
r4.shape
r4

r5 = np.random.randint(100, 300, size=(8,10))
r5

#3 Dim
r6 = np.random.randint(1, 10, size=(2, 3, 4))
r6

#4 Dim
n7 = np.random.randint(1, 10, size= (2,3,4,5))
n7

n7.shape





r4 = np.random.randint(1, 30, size=(3,4))
r4

r4.shape

r4 = r4.reshape(2,6)
r4.shape
r4

r4 = r4.reshape(6,2)
r4.shape
r4




r4 = np.random.randint(1, 30, size=10)
r4

r4[0]

r4[0:5]
r4[0:3]

r4[:4]
r4[4:]
r4[4:-2]



r4 = np.random.randint(1, 30, size=(5,4))
r4

r4.shape

r4[0:2,:]

r4[-2:, :]
r4
r4[0:2,1:3 ]
r4[1:4, 1:3]

r4[-1,-2:]


r4 = np.random.randint(1, 30, size=(2,5,4))
r4

r4[:,1:3,1:3 ]
r4
r4[:,:,0:2]



r4 = np.random.randint(1, 30, size=(5,4))
r4

r4[:,::2]



import numpy as np

a1 = np.arange(20)
a1

a2 = np.arange(20, 40)
a2

a3 = np.arange(10, 30, 5)
a3


a4 = np.zeros((3,4))
a4

a4 = a4.astype('int')
a4

a4 = a4.astype('float')
a4

a5 = np.ones((3,4))
a5

a6 = np.eye(3,3)
a6


a7 = np.linspace(0, 10, num=5)
a7


r5 = np.random.randint(10, 50, size=(5,7))
r5

np.sum(r5)
np.mean(r5)
np.median(r5)
np.std(r5)
np.var(r5)

r5 = np.random.randint(1, 5, size=(3,4))
r5
np.sum(r5, axis=0)
np.sum(r5, axis=1)
np.mean(r5, axis=0)
np.mean(r5, axis=1)
r5

np.floor([1.2,1.6])
np.ceil([1.2,1.6])
np.trunc([1.2,1.6])
np.round([1.2,1.6])

np.floor([-1.2,-1.6])
np.ceil([-1.2,-1.6])
np.trunc([-1.2,-1.6])
np.round([-1.2,-1.6])

np.round([1.33245, 3.23421],3)


np.abs([-1.2])



n1 = np.random.randint(1, 9, size=(3,4))
n2 = np.random.randint(1, 9, size=(3,4))

n3 = np.concatenate([n1,n2], axis=0)

n1
n2
n3


n4 = np.concatenate([n1,n2], axis=1)
n4


n5 = np.split(n4,2, axis=1)
n4

type(n5)

len(n5)

n5[0]
n5[1]

type(n5[0])

n5[0].shape

r1 = n5[0]

r1[1:,1:]

n5[0][1:,1:]


n6 = np.random.randint(1, 100, size=100)

n6

n6>30
n6<30
n6<=40


np.all(n6<100)

np.any(n6<10)

n6 = np.random.randint(1, 10, size=5)
n6
np.sum(n6<5)


n7 = np.array([10, 20, None, None, 40])
n7

n7==None 

np.sum(n7==None)

n6
n6.sort()
n6

n8 = np.random.randint(1, 10, size=50)

np.sum((n8<6) & (n8>3))



import matplotlib.pyplot as plt
import numpy as np


l1 = np.random.randint(1, 101, size=1000)

plt.hist(l1)

np.mean(l1)
np.median(l1)
np.std(l1)


l2 = np.random.normal(100, 10, size=10000)
plt.hist(l2)

np.mean(l2)
np.median(l2)
np.std(l2)


l3 = np.random.binomial(1, p=.2, size=100)
plt.hist(l3)
np.mean(l3)
np.median(l3)
np.std(l3)

l3
l2
# Pandas

l4= np.random.poisson(0.9, size=100)
plt.hist(l4)


l5= np.random.uniform(0,10, size=100)
plt.hist(l5)



l6= np.random.exponential(0.9, size=100)
plt.hist(l6)














































































