#!/usr/bin/env python
# coding: utf-8

# In[8]:


#cleaning the data
#import libraries
import pandas as pd
import numpy as np


# In[10]:


#read data in pandas dataframe
data = pd.read_csv(r'C:\Users\zakbh\OneDrive\Desktop\rainfall prediction\austin_weather.csv')


# In[11]:


data = data.drop(['Events', 'Date', 'SeaLevelPressureHighInches', 'SeaLevelPressureAvgInches'], axis=1)


# In[17]:


data = data.replace('T', 0.0)
data = data.replace('-', 0.0)

data.to_csv(r'C:\Users\zakbh\OneDrive\Desktop\rainfall prediction\austin_final.csv')

