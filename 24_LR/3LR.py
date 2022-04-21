#Topic: Simple Linear Regression - Area - Rent
#-----------------------------
#https://raw.githubusercontent.com/DUanalytics/pyAnalytics/master/8B-LM/lm_slr_area.py
#libraries
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns
# Load the diabetes dataset

url = "https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/slr1.csv"
data = pd.read_csv(url)
#data = pd.read_csv('data/slr1.csv')
data.columns
data



#data has features, target has DV value Use only one feature
X = data
X.columns
X = X.drop(['Age'], axis =1)
X=X.values

X.shape

y = data['Age'].values
y=y.reshape(-1,1)
y.shape



from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.05)


#%%%
from sklearn import linear_model
lm = linear_model.LinearRegression()

model1 = lm.fit(xtrain, ytrain)

print(model1)

model1.score(xtrain,ytrain)  #R2

y_pred1 = model1.predict(xtest)
y_pred1
ytest




import matplotlib.pyplot as plt

plt.scatter(X,y)
plt.scatter(X,y_pred1)
#The mean squared error

mean_squared_error(y,y_pred1)
r2_score(y, y_pred1)

print('Variance score: %.2f' % r2_score(y, y_pred1))
# Plot outputs  : select all at once and run
plt.scatter(X, y,  color='black')
plt.plot(X, y_pred1, color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show();


#%% Model 2
import statsmodels.api as sm
X,y
model2 = sm.OLS(X, y).fit()
model2.summary()
predictions2 = model2.predict(X)
predictions2
model2.summary()
# add constant
X2 = sm.add_constant(X) #Adds a column of ones to an array
model3 = sm.OLS(y, X2).fit() #output, input
model3.summary()
predictions3 = model3.predict(X2)
predictions3

#%% Model4
#https://www.learndatasci.com/tutorials/predicting-housing-prices-linear-regression-using-python-pandas-statsmodels/

from statsmodels.formula.api import ols
data.columns
model4 = ols('Y ~ X', data=data).fit()
model4.summary()
#diagnostic plots
fig, ax = plt.subplots()

fig = sm.graphics.plot_fit(model4,"X", ax=ax)
ax.set_ylabel("Rent")
ax.set_xlabel("Area")
ax.set_title("Linear Regression")

plt.show();
