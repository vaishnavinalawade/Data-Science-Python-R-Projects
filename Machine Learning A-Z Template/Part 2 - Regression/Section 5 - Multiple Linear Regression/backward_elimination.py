# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:39:30 2020

@author: Vaish
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,3] = labelencoder_X.fit_transform(X[:,3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()
X = X[:,1:]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)



import statsmodels.api as sm

X = np.append(arr= np.ones((50,1)), values= X, axis=1)

def backwardElimination(x, SL):
  numVars = len(x[0])
  temp = np.zeros((50,6)).astype(int)
  for i in range(0, numVars):
    regressor_OLS = sm.OLS(y,x).fit()
    maxVar = max(regressor_OLS.pvalues).astype(float)
    adjR_before = regressor_OLS.rsquared_adj.astype(float)
    if maxVar>SL:
      for j in range(0, numVars-i):
        if(regressor_OLS.pvalues[j]==maxVar):
          temp[:,j] = x[:,j]
          x = np.delete(x,j,1)
          temp_regressor = sm.OLS(y,x).fit()
          adjR_after = temp_regressor.rsquared_adj.astype(float)
          if(adjR_before>=adjR_after):
            x_rollback = np.hstack((x, temp[:, [0,j]]))
            x_rollback = np.delete(x_rollback, j,1)
            print(regressor_OLS.summary())
            return x_rollback
          else:
            continue
    regressor_OLS.summary()
    return x
SL = 0.05
X_opt = X[:, [0,1,2,3,4,5]]
X_Modeled = backwardElimination(X_opt, SL)
          
          
          
          
          
          
          
    
    
    
    
    
    
    
    
    
    