#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv(r'E:\pdf files\logisticheart\framingham.csv')
df


# In[2]:


df['totChol'].fillna(233.9, inplace=True) 
df['BMI'].fillna(25.6, inplace=True)
df['heartRate'].fillna(75.86, inplace=True)
df['glucose'].fillna(74.4, inplace=True)
df['BPMeds'].fillna(0, inplace=True)
print("***Count NaN in each column of a DataFrame***")
print("Nan in each columns" , df.isnull().sum(), sep='\n')


# In[3]:


#logistic regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix,accuracy_score

feature_cols = ['totChol', 'sysBP', 'diaBP', 'glucose']
X = df[feature_cols] # Features
y = df.TenYearCHD

 

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)
logreg = LogisticRegression()
logreg.fit(X_train,y_train)

y_pred=logreg.predict(X_test)


# In[4]:


from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
cnf_matrix


# In[9]:


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
class_names=[0,1] # name of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')


# In[10]:


print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred))
print("Recall:",metrics.recall_score(y_test, y_pred))


# In[21]:


#multi linear regression
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# In[24]:


X = pd.DataFrame(np.c_[df['totChol'], df['age'], df['sysBP'],df['cigsPerDay'],df['diaBP'], df['glucose'],df['heartRate'],df['BMI']], columns=['totChol','age', 'sysBP','cigsPerday', 'diaBP', 'glucose','heartRate','BMI'])
Y = df['TenYearCHD']


# In[25]:


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state=9)


# In[26]:


lin_reg_mod = LinearRegression()


# In[27]:


lin_reg_mod.fit(X_train, y_train)


# In[28]:


pred = lin_reg_mod.predict(X_test)


# In[29]:


test_set_rmse = (np.sqrt(mean_squared_error(y_test, pred)))

test_set_r2 = r2_score(y_test, pred)


# In[30]:


print(test_set_rmse)
print(test_set_r2)


# In[ ]:




