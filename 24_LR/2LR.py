#Topic ---- Dividing Data into Train and Test 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data

from sklearn.linear_model import LinearRegression

mtcars = data('mtcars')

data=mtcars

data.head()
data.columns
data.dtypes
data.shape



model = LinearRegression()



ds= mtcars[['mpg', 'hp']]

ds.head()


plt.scatter(ds['mpg'],ds['hp'] )


x= ds['mpg'].values.reshape(-1,1)
x.shape

y=ds['hp'].values

x.shape
y.shape


from sklearn.model_selection import train_test_split
x_train, x_test, y_train,  y_test = train_test_split(x,y, test_size=0.2)

x_train.shape
y_train.shape

x_test.shape
y_test.shape

model.fit(x_train, y_train)

r_sq = model.score(x,y)
r_sq

'''
r_sq = model.score(x_test,y_test)
r_sq
'''

ypred= model.predict(x_test)
ypred.shape
y.shape


plt.scatter(x_train,y_train)
plt.scatter(x_test,y_test)
plt.scatter(x_test, ypred)



x_pred= np.array([25, 5]).reshape(-1,1)
x_pred.shape

ypred1 = model.predict(x_pred)
ypred1

plt.scatter(x,y)
plt.scatter(x_test,y_test)
plt.scatter(x_pred, ypred1)



model.score(x_train,y_train)
model.score(x_test,y_test)





#Multi Linear Regression

from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data

from sklearn.linear_model import LinearRegression

mtcars = data('mtcars')

data=mtcars

data.head()
data.columns
data.dtypes
data.shape


model = LinearRegression()


ds= mtcars[['mpg', 'wt', 'hp']]

ds.head()


plt.scatter(ds['mpg'],ds['hp'] )

plt.scatter(ds['mpg'],ds['wt'] )


x= ds[['hp','wt']].values

y=ds['mpg'].values

x.shape
y.shape


x_train, x_test, y_train,  y_test = train_test_split(x,y, test_size=0.1)

x_train.shape
y_train.shape

x_test.shape
y_test.shape



model.fit(x_train, y_train)

r_sq = model.score(x_test,y_test)
r_sq


ypred= model.predict(x_test)
ypred.shape
y.shape

x_test

x_pred= np.array([[300, 4.5], [350, 5.6]])
x_pred.shape

ypred1 = model.predict(x_pred)
ypred1

plt.scatter(x,y)
plt.scatter(x_test,y_test)
plt.scatter(x_pred, ypred1)



model.score(x_train,y_train)
model.score(x_test,y_test)

#%%% Sample by number

s1 = data.sample(10)
s1
#%%%


from sklearn.model_selection import train_test_split


X=np.arange(10).reshape((10, 1))
y=range(10)
X
y




#split X and y
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size= 0.30)
X_train
y_train
X_test
y_test

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(x_test)
y_pred
y_test



#%%%


#%%%
'''
R-squared (R2) is a statistical measure that represents the proportion of the 
variance for a dependent variable that's explained by an independent variable 
or variables in a regression model. Whereas correlation explains the strength 
of the relationship between an independent and dependent variable, R-squared 
explains to what extent the variance of one variable explains the variance 
of the second variable.
'''
'''
The F value is the ratio of the mean regression sum of squares divided 
by the mean error sum of squares. Its value will range from zero to an 
arbitrarily large number. The value of Prob(F) is the probability that the 
null hypothesis for the full model is true (i.e., that all of the regression 
coefficients are zero).
'''

import statsmodels.api as sm
import matplotlib.pyplot as plt
from pydataset import data

mtcars = data('mtcars')
mtcars.columns

df1 = mtcars[['wt','hp', 'mpg']]
df1.head(5)

from statsmodels.formula.api import ols

MTmodel1 = ols("mpg ~  wt", data=mtcars).fit()
print(MTmodel1.summary())

MTmodel1 = ols("mpg ~  wt + hp", data=mtcars).fit()
print(MTmodel1.summary())


predictionM1 = MTmodel1.predict()
predictionM1

#https://www.datarobot.com/blog/ordinary-least-squares-in-python/

'''
The CCPR plot provides a way to judge the effect of one regressor on the 
response variable by taking into account the effects of the other independent 
variables. The partial residuals plot is defined as Residuals+BiXi versus Xi.
Component-Component plus Residual (CCPR) Plots¶

The CCPR plot provides a way to judge the effect of one regressor on the 
response variable by taking into account the effects of the other independent 
variables. The partial residuals plot is defined as Residuals+BiXi  
versus Xi. The component adds BiXi versus Xi to show where the fitted line
would lie. Care should be taken if Xi is highly correlated with any of the 
other independent variables. If this is the case, the variance evident in 
the plot will be an underestimate of the true variance.

Since we are doing multivariate regressions, we cannot just look at 
individual bivariate plots to discern relationships. Instead, we want 
to look at the relationship of the dependent variable and independent 
variables conditional on the other independent variables. We can do this 
through using partial regression plots, otherwise known as added variable plots.
'''
fig, ax = plt.subplots(figsize=(12, 8))
fig = sm.graphics.plot_ccpr(MTmodel1, "hp", ax=ax)

fig = plt.figure(figsize=(12, 8))
fig = sm.graphics.plot_ccpr_grid(MTmodel1, fig=fig)

#%%%
#fig, ax = plt.subplots()
#fig = sm.graphics.plot_fit(MTmodel1, 0, ax=ax)
#----

from sklearn.metrics import r2_score,mean_squared_error

IV = df1[['wt','hp']].values
IV

DV= df1['mpg'].values
DV

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(IV, DV,test_size=0.2)

x_train.shape
y_train.shape



from sklearn import linear_model

MTmodel2a = linear_model.LinearRegression()

MTmodel2a.fit(x_train, y_train)  #putting data to model

y_pred = MTmodel2a.predict(x_train)

#mean_squared_error(DV_test, predicted2a)
r2_score(y_train, y_pred)  #???
mean_squared_error(y_train, y_pred)




x_train.shape
y_train.shape

import pandas as pd
xdf = pd.DataFrame(x_train)
xdf['Result'] =pd.DataFrame(y_train)
xdf

from statsmodels.formula.api import ols

MTmodel2a = ols("Result ~ 0 + 1", data= xdf).fit()

MTmodel2a.summary()  #no summary in sklearn

MTmodel2a.intercept_
MTmodel2a.coef_

predicted2a = MTmodel2a.predict(IV_test)
predicted2a

DV_test

#The mean squared error
from sklearn.metrics import mean_squared_error, r2_score

mean_squared_error(DV_test, predicted2a)
r2_score(DV_test, predicted2a)  #???

#%%%
# what to LM
# Predicting Continuous, Finding relationship between variables
# Steps : load data, split : DV & IV ; Train and test set
# Load the libraries
# create model : function + IV & DV from Train
# see r2, adjst R2, coeff, significant, other model 
# predict : Model + IV_test -> predicted_y
# rmse : predicted_y - actual_y : as less as possible
# R2 ??
# check for assumption - linear, normality, homoscedascity, multi-collinearity, auto-collinearity

#%%%% Links
#https://pythonprogramminglanguage.com/training-and-test-data/

#%%% Links
#https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html


