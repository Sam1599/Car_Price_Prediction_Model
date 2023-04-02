#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pickle
from sklearn.metrics import mean_absolute_error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv(r'C:\Users\samyu\Downloads\CarPrice.csv')
data.head()


# In[23]:


data.isnull().sum()


# In[24]:


data.info()


# In[25]:


print(data.describe())


# In[26]:


data.CarName.unique()


# In[31]:


predict = "price"
data = data[["symboling", "wheelbase", "carlength",
             "carwidth", "carheight",
             "enginesize",
             "horsepower", "peakrpm",
             "citympg", "highwaympg", "price"]]
x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)

model = DecisionTreeRegressor()
model.fit(xtrain, ytrain)
predictions = model.predict(xtest)

model.score(xtest, predictions)


# In[ ]:


data.info()


# In[ ]:

pickle.dump(model, open('model.pkl', 'wb'))
