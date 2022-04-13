# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 20:51:04 2022

@author: vikas
"""

a = input("Enter a->")

s = "hi"
b =10
c =12.4

a=10
b=20
c = a+b

x = input("Enter a->")

y = input("Enter y->")

x + y

#String to Number
# Type Conversion or Type Casting

x = int(input("Enter a->"))


x = input("Enter x->")
x = int(x)


y = int(input("Enter y->"))

z = x+y
z


int(input("Enter y->"))


a = 20
type(a)

s = "age is "

s + str(a)


s = '10'

int(s)
float(s)

i= 10
str(i)
float(i)

f= 10.3
str(f)
int(f)



c = 'A'
ord(c)


c = 'Z'
ord(c)

c = '!'
ord(c)


i = 65
chr(i)


test = 'AxSdSwRtdSfDD'

t = ''

for i in test:
    if(ord(i)>=65 and ord(i)<=90):
        t=t+i

print(t)


#Airthmetic Operators

x = 10

print(x+1)

print(x-1)

print(x/2)

print(x*3)

print(x**3)

print(x**(1/2))

print(x % 2)


a = int(input("Enter value-> "))
a=20
if (a % 2 == 0):
    print("even")
else:
    print("Odd")


x = 10

x = x + 1

x = x*2

#Comparative Operators

a=20
b=10
c=20

a == b
a == c

a < b
a>b

a<= b

a>=b

a != b


#Boolean - True or False

t = True
f = False


a= 77

a>=65 and a<=90


'''
AND
X Y O
0 0 0
0 1 0
1 0 0
1 1 1

OR
X Y O
0 0 0
0 1 1
1 0 1
1 1 1

Not
X O
0 1
1 0

'''

t = True
not t


a = 10
b = 20
c = 30

a <= b and b >= c

a <= b or b >= c


# String Handling

h = "Hello"
w = "World"

h+w

h + " " + w

len(h)

s ="hello"

s.capitalize()

s = s.upper()

s =s.lower()

s

s = "Hello Java"

s = s.replace("Java", "Python")


name = input("Enter Your Name->")

name  = name.strip()



# Combinatioal/ Extended Datatypes

# List, Set, Dictionary, Tuple

# Mutable, Indexed, Ordered, Hetergeneous, Unique Values, Key-Value Pair


l1 = []

l2 = [20,23,10,22,55, 23]
print(l2)


#Indexed

l2[0]
l2[1]
l2[2]
l2[3]
l2[4]
l2[5] #IndexError: list index out of range


#Hetrogeneous

l3 = [10, 303.2, True, "String"]

l3
l3[1]
l3[3]

#Mutable or Changable

l2[0] = 33
l3[2] = "VK"

print(l3)



r1 = list(range(10))
r2 = list(range(20))
r2
r3 = list(range(11, 21))
r3
r4 = list(range(11, 51, 5))
r4

r5 = list(range(100, 200))
r5

r5[0]
r5[1]

for i in r5:
    print(i*6)


l2

l2.append(44)
l2

l2.extend([555,333])
l2

l2.pop()
l2.pop(2)
l2

l2.remove(22)
l2

l2.remove(22)
l2

l2

l2.sort()
l2

l2.reverse()
l2

r5.reverse()
r5



#Set

# Mutable, Non Indexed, Ordered, Hetergeneous, Unique Values, No Key-Value Pair

s1 = {10}

# Ordered
s2 = {30,50,10,20,40}
s2

# Unique Values

s3 = {20,30,30,10,20,90,30,20}
s3

# Non- Indexed

s3[0] #TypeError: 'set' object is not subscriptable

for i in s3:
    print(i)

#Hetrogeneous

s4 = {"VK", 22, 43.2, True}
s4


#Mutable

s3
s3.add(122)
s3
s3.add(22)
s3
s3.add(122)
s3

s3.update([22,33,44,66])
s3

s3.pop()

s3
s3.remove(30)
s3


s3.remove(44)
s3

s3.remove(44) #  KeyError: 44 Not available

s3
s3.discard(22)
s3

s3.discard(22) # No show any error even the keyvalue is not available
s3



teamA = {'India', 'Australia','Pakistan', 'England'}
teamB = {'Bangladesh', 'New Zealand', 'West Indies', 'India'}

teamA.union(teamB)

teamA.intersection(teamB)

teamA.difference(teamB)




# Tuple

# Non Mutable, Indexed, No Ordered, Hetergeneous, No Unique Values, No Key-Value Pair


t1 = ()
t2 = (20,301,2,44,34)
t2

t2[0]
t2[4]
t2[5] #Should be in a range

t3 = ('Vk', 22, 4.2, True)
t3

t2[2] =232 #TypeError: 'tuple' object does not support item assignment

t2.append(10) # AttributeError: 'tuple' object has no attribute 'append'



r1 = tuple(range(101, 201))
r1[0] =20



#teamA - teamB

teamA.difference()


#Dictionary
# Mutable, No Indexed, No Ordered, Hetergeneous, No Unique Values, Key-Value Pair

d1 = {}

#Key Value Paired
d2 = {'rno':1, 'name':'VK'}
d2

#Hetrogeneous


car = {'brand':'Honda', 'color':'white', 'model':'Jazz'}
car

#Not Indexed
car[1]

car['brand']

car['color']

car['model']


car.keys()
car.values()



rno = list(range(1,100))

stud = {'rno':rno}

stud['rno']


#Mutable
car['year'] = 2020

car

car['year'] = 2021
car



car

car.pop('brand')

car

car.popitem()

car


car.clear()
car

del car

l1 = [20,22,11,99,88]

l1

l2= l1

l1.pop()
l2.append(222)


l3 = l1.copy()

l3.append(44)




























































































































































































