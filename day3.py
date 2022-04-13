# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 21:01:19 2022

@author: vikas
"""


#Conditions

'''
if (condition):
    {
     statement
     }
'''

a=10
b=20

if (a<b):
    print("a is lesser")



if (a>b):
    print("a is lesser")



if (0):
    print("a is lesser")



if (-11):
    print("a is lesser")


if (True):
    print("a is lesser")




if (a<b):
    print("a is lesser")
else:
    print("a is greater")




'''
if()
{

}
else
{

 
}




'''


marks = int(input("Enter Marks"))

if (marks>90):
    print("A")
elif(marks>80 and marks<=90):
    print("B")
elif(marks>70 and marks<=80):
    print("C")
elif(marks>60 and marks<=70):
    print("D")
else:
    print('Fail')




#Looping


teamA = ['India', 'Australia','Pakistan', 'England']   # 4elements   list index 0-3

teamA[0]

teamA[1]

teamA[2]


for i in teamA:
    print(i)

r1 = list(range(1,11))

r1

for i in r1:
    print(i*2)


j=2
for i in range(1,11):
    print("{0} * {1} = {2}".format(j,i, i*j))
    

for j in range(2,5):
    for i in range(1,11):
        print("{0} * {1} = {2}".format(j,i, i*j))
    


print('hello','world', sep='\n')
print("hello", end='')
print("world")



print("hello's")




while(True):
    print('Hello')


cnt=1

while(cnt<=10):
    print(cnt)
    cnt =cnt+1


j = 1
while(j<=10):
    i=1
    while(i<=10):
        print("{0} * {1} = {2}".format(j,i, i*j))
        i=i+1
    j=j+1



#break
#Continue


import numpy as np
a = np.random.randint(0, 10000, size=100)
a

cnt=1
for i in a:
    print(cnt)
    cnt=cnt+1
    if (i == 9803):
        print("number searched")
        break

for i in a:
    break


teamA = ['India', 'Australia','Pakistan', 'England']

for t in teamA:
    if(t =='Pakistan'):
        print(t, "in loop")
        break
    print(t, 'out loop')


for t in teamA:
    if(t =='Pakistan'):
        print(t, "in loop")
        #continue
    print(t, 'out loop')



pswd = 'vikas'

while(True):
    p = input("Enter passwds")
    if(p==pswd):
        break
    print("enter correct Password")
    continue


#Functions

#Defination
def op():
    a=10
    b=20
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)


op()
op()
op()


def op1(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

op1(10,20)


op1(20,30)

op1(33,22)




def printHello(name):
    print("Hello", name)


printHello('VK')


printHello('MK')



def emp(eid, name, email, phone):
    print(eid, name, email, phone)



emp(10, 'VK', 's',9999)

emp(10, 'VK', 's')




def emp(eid, name, email, phone= 99999):
    print(eid, name, email, phone)



emp(10, 'VK', 's')

emp(10, 'VK', 's',888999)




l = np.random.randint(10, 200, size=22)
l

max(l)


#declaration
#defination
#calling

def maxlist(lst):
    m=0
    for n in lst:
        if(n>m):
            m=n
    return(m)
    

a = maxlist(l)

print(a)



# lambda


def f(x):
    return(x**2)


f(10)
f(88)


fl = lambda x : x**2

fl(2)

fl1 = lambda x,y: x*y

a = fl1(2,3)
a


l1 = [1,2,3,4,5]

sq=[]
for i in l1:
    sq.append(i**2)

sq

s1 = lambda x: x**2

sq1 = list(map(s1, l1))
sq1


l1 = ['vk', 'ak', 'mk', 'yk']

s = lambda x:x.upper()

list(map(s,l1))


s1=[]
for i in l1:
    s1.append(s(i))
s1


#filter

l1 = [2,3,1,4,5,3,5,4]

l = lambda x: x%2==0

list(filter(l, l1))


l1 = [-2, 6, -3, 5, 6, -7]

l = lambda x: x>=0
list(filter(l, l1))









































































































