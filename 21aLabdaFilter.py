# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 19:13:06 2020

@author: vikas
"""

#Lambda

def f(x):
    return (x**2)

f(3)
f(9)

f_lambda = lambda x : x**2

f_lambda(3)

a = f_lambda(3)

print (a)

print(f_lambda(4))

print(f_lambda(6))



f1_lambda = lambda x,y : x*y

a = f1_lambda(3,4)
a


print (a)



def f(x,y,z):
    return (x+y+z)


f2_lambda = lambda x,y,z : x+y+z
print (f2_lambda(1,2,3))




dict1 = {'name':['Amit', 'Amy',' Tina'], 'year': [2012, 2013, 2014]}
df2 = pd.DataFrame(dict1, index = [0,1,2])
df2


caps = lambda x : x.upper()

caps('vikas')


df2.name = df2['name'].apply(caps)
df2








#Lambda


# Python code to illustrate cube of a number  
# showing difference between def() and lambda(). 

def cube(y): 
    return y*y*y; 
  
  
cube(5)  
cube(54)  


    
g = lambda x: x*x*x 

print(g(7)) 
  
print(cube(7)) 







#Map
squared = []

items = [1, 2, 3, 4, 5]

for i in items:
    squared.append(i**2)

squared

#Map allows us to implement this in a much simpler and nicer way. Here you go:


sq= lambda x: x**2

squared1 = list(map(sq, items))
squared1


# Python code to illustrate  
# map() with lambda()  
# to get double of a list. 
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 

final_list = list(map(lambda x: x*2 , li)) 
print(final_list) 



'''
#Most of the times we use lambdas with map so I did the same. Instead of a list of inputs we can even have a list of functions!

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]

for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
'''



#Filter
number_list = list(range(-5, 5))
number_list


less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]


# Python code to illustrate 
# filter() with lambda() 
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 

final_list = list(filter(lambda x: (x%2 == 0) , li)) 

print(final_list) 


def f1(x):
    return(x%2 == 0)



# Python code to illustrate  
# reduce() with lambda() 
# to get sum of a list 


from functools import reduce

li = [5, 8, 10, 20, 50, 100] 

s1 = reduce(lambda x, y: x + y, li) 

print (s1) 




#Reduce
#Reduce is a really useful function for performing some computation on a list and returning the result. It applies a rolling computation to sequential pairs of values in a list. For example, if you wanted to compute the product of a list of integers.

#So the normal way you might go about doing this task in python is using a basic for loop:

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

# product = 24



from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Output: 24













df.dtypes






















