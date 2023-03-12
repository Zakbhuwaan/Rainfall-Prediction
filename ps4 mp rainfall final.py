#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# In[19]:


#read clean data
data = pd.read_csv(r'C:\Users\zakbh\OneDrive\Desktop\rainfall prediction\austin_final.csv')


# In[20]:


X = data.drop('PrecipitationSumInches', axis=1)

Y = data['PrecipitationSumInches']
Y = Y.values.reshape(-1,1)


# In[21]:


day_index = 798
days = [i for i in range(Y.size)]


# In[22]:


clf = LinearRegression()
clf.fit(X, Y)


# In[26]:


inp = np.array([[74], [60], [45], [67], [49], [43], [33], [45],
                [57], [29.68], [10], [7], [2], [0], [20], [4], [31]])


# In[29]:


inp = inp.reshape(1, -1)


# In[30]:


print('The precipitation in inches for the input is:', clf.predict(inp))


# In[33]:


print('the precipitation trend graph:=')
plt.scatter(days, Y, color='g')
plt.scatter(days[day_index], Y[day_index], color='r')
plt.title('precipitation level')
plt.xlabel('days')
plt.ylabel('Precipiation in inches')

plt.show()


# In[36]:


x_f = X.filter(['TempAvgF', 'DewPointAvgF', 'HumidityAvgPercent',
                'SeaLevelPressureAvgInches', 'VisibilityAvgMiles',
                'WindAvgMPH'], axis=1)


# In[47]:


print('Precipitation Vs Selected Attributes Graph: ')
for i in range(x_f.columns.size):
    plt.subplot(3,2, i+1)
    plt.scatter(days, x_f[x_f.columns.values[i][:100]], color='g')
    plt.scatter(days[day_index], x_f[x_f.columns.values[i]]
            [day_index], color='r')
                      
    plt.title(x_f.columns.values[i])
            
plt.show()

