# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:02:51 2022

@author: vikas
"""

import matplotlib.pyplot as plt

Year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
Unemployment_Rate = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
Unemployment_Rate1 = [1.8,2,8,4.2,6.0,7,3.5,5.2,7.5,5.3]


#Line Plot

plt.plot(Year, Unemployment_Rate )
plt.title("Year vs Unemployment_Rate ")
plt.xlabel('Year')
plt.ylabel('Unemployment_Rate ')
plt.show()




plt.plot(Year, Unemployment_Rate, color ='r', marker = '*', markersize=12, label = 'UR1')
plt.plot(Year, Unemployment_Rate1, color = 'y', marker = 'o', markersize= 12 , label= 'UR2')
plt.title("Year vs Unemployment_Rate", fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Unemployment_Rate', fontsize=12)
plt.legend()
plt.grid()
plt.show()



col = ['#76AF84', '#6D4735', '#ED6420', '#A00BEA']

plt.plot(Year, Unemployment_Rate, color =col[0], marker = '*', markersize=12, label = 'UR1')
plt.plot(Year, Unemployment_Rate1, color = col[3], marker = 'o', markersize= 12 , label= 'UR2')
plt.title("Year vs Unemployment_Rate", fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Unemployment_Rate', fontsize=12)
plt.legend()
plt.grid()
plt.show()


import pandas as pd

Year = [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010]
Unemployment_Rate = [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
Unemployment_Rate1 = [1.8,2,8,4.2,6.0,7,3.5,5.2,7.5,5.3]

df = pd.DataFrame({'Year':Year,'Unemployment_Rate':Unemployment_Rate, 'Unemployment_Rate1':Unemployment_Rate1})
df

plt.plot(df.Year, df.Unemployment_Rate, color =col[0], marker = '*', markersize=12, label = 'UR1')
plt.plot(df.Year, df.Unemployment_Rate1, color = col[3], marker = 'o', markersize= 12 , label= 'UR2')
plt.title("Year vs Unemployment_Rate", fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Unemployment_Rate', fontsize=12)
plt.legend()
plt.grid()
plt.show()



#Bar Plot



Country = ['USA','Canada','Germany','UK','France']
GDP_Per_Capita = [45000,42000,52000,49000,47000]

plt.bar(Country,GDP_Per_Capita, color =col )
plt.title('Country vs GDP_Per_Capita')
plt.xlabel('Countries')
plt.ylabel('GDP_Per_Capita')
plt.grid()
plt.show()



import numpy as np
xl = list(range(1, 101))
yl = np.random.randint(0, 70, size=100)

plt.plot(xl, yl)

ls = np.linspace(0, 100, 11)
ls



ls1 = np.linspace(0, 100, 11)
ls1
plt.plot(xl, yl)
plt.xticks(ls)
plt.yticks(ls1)




#Scatter Plot


x = np.random.normal(25,5, size=100)
y = np.random.randint(100, 120, size=100)

plt.scatter(x,y)



x = list(range(1, 101))
y = np.random.randint(1, 1000, size=100)

len(x)
len(y)

plt.scatter(x,y)




x = [1,3,4,5,7,8,9]
y = [10, 15, 14, 20, 30, 23, 28]
plt.scatter(x,y)


from pydataset import data

mt = data('mtcars')

mt.columns
mt.head()


plt.scatter(mt['hp'],mt['mpg'])
plt.ylabel('MPG')
plt.xlabel('HP')



plt.scatter(mt['hp'],mt['mpg'], c = mt['cyl'], s = mt.disp)
plt.ylabel('MPG')
plt.xlabel('HP')
plt.legend(loc='upper left')



import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

df.dtypes

df.head()

sns.scatterplot(df.total_bill, df.tip)

sns.scatterplot(data=df, x="total_bill", y="tip", hue="smoker")

sns.scatterplot(data=df, x="total_bill", y="tip", hue="time", style="smoker")

sns.scatterplot(data=df, x="total_bill", y="tip", hue="size", style="smoker")




df.dtypes
sns.scatterplot(
    data=df, x="total_bill", y="tip", hue = 'size', size="size",
    legend="full"
)




index = pd.date_range("1 1 2000", periods=100, freq="m", name="date")
index

data = np.random.randn(100, 4).cumsum(axis=0)
data

wide_df = pd.DataFrame(data, index, ["a", "b", "c", "d"])

sns.scatterplot(data=wide_df)


#Box Plots


import matplotlib.pyplot as plt
import numpy as np

d1 = np.random.normal(50, 30, size=1000)

print(d1.min(), d1.max(), d1.std(), d1.mean()

plt.boxplot(d1)


d2 = d1[(d1>-25) & (d1<125)]

plt.boxplot(d2)


import seaborn as sns
tips = sns.load_dataset("tips")
tips.columns
ax = sns.boxplot(x=tips["total_bill"])
ax = sns.boxplot(x=tips["tip"])

sns.scatterplot(tips["total_bill"], tips["tip"])

tip = tips[tips['tip']<6]['tip']
tb = tips[tips['total_bill']<40]['total_bill']

sns.scatterplot( tb,tip)


# Heat Map

import numpy as np
import seaborn as sns

uniform_data = np.random.rand(10, 10)
uniform_data

df = pd.DataFrame(uniform_data)
df
sns.heatmap(df)

from pydataset import data
mtcars = data('mtcars')
mtcars[['mpg','wt','hp','disp']]. head()

mtcorr = mtcars.corr()

sns.heatmap(mtcorr, annot=True, fmt = '.1g', cmap = 'plasma')













































































































