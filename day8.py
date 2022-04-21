# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 21:33:32 2022

@author: vikas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([5,15,25,35,45,55])
y = np.array([5,20,14,32,22,38])  #1 dim

x
y

plt.scatter(x,y)

from sklearn.linear_model import LinearRegression