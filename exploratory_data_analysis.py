#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv(r'E:\pdf files\logisticheart\framingham.csv')
df.head(10)


# In[3]:


df.shape


# In[5]:


df.info()


# In[7]:


df['gender'] = df['gender'].astype('category')
df['currentSmoker'] = df['currentSmoker'].astype('category')
df['BPMeds'] = df['BPMeds'].astype('category')
df['prevalentStroke'] = df['prevalentStroke'].astype('category')
df['prevalentHyp'] = df['prevalentHyp'].astype('category')
df['diabetes'] = df['diabetes'].astype('category')
df['TenYearCHD'] = df['TenYearCHD'].astype('category')


# In[15]:


import statistics as stat
print(stat.mode(df['age']))
print(stat.mode(df['cigsPerDay']))
print(stat.mode(df['totChol']))
print(stat.mode(df['sysBP']))
print(stat.mode(df['diaBP']))
print(stat.mode(df['heartRate']))
print(stat.mode(df['glucose']))


# In[8]:


df.info()


# In[9]:


df.describe()


# In[10]:


df.TenYearCHD.unique()


# In[11]:


df.TenYearCHD.value_counts()


# In[3]:


df['totChol'].fillna(233.9, inplace=True) 
df['BMI'].fillna(25.6, inplace=True)
df['heartRate'].fillna(75.86, inplace=True)
df['glucose'].fillna(74.4, inplace=True)
df['BPMeds'].fillna(0, inplace=True)
print("***Count NaN in each column of a DataFrame***")
print("Nan in each columns" , df.isnull().sum(), sep='\n')


# In[ ]:




