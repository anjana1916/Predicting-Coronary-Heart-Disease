#!/usr/bin/env python
# coding: utf-8

# In[1]:


#classifiers
import pandas as pd
df = pd.read_csv(r'E:\pdf files\logisticheart\framingham.csv')
df


# In[2]:


df['totChol'].fillna(233.9, inplace=True) 
df['BMI'].fillna(25.6, inplace=True)
df['heartRate'].fillna(75.86, inplace=True)
df['glucose'].fillna(74.4, inplace=True)
df['BPMeds'].fillna(0, inplace=True)


# In[3]:


print("***Count NaN in each column of a DataFrame***")
print("Nan in each columns" , df.isnull().sum(), sep='\n')


# In[19]:


#bayesian classifier
from __future__ import division, print_function
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import csv
import scikitplot as skplt
from sklearn import preprocessing

from pylab import scatter,show,plot
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score

from sklearn.metrics import precision_score,recall_score,accuracy_score


data = df[['gender','currentSmoker','BPMeds','prevalentStroke','prevalentHyp','diabetes','TenYearCHD']]


print('KMeans Labelling')
n_clusters=2
kmeans = KMeans(n_clusters).fit(data)
class_labels = kmeans.labels_


X_train, X_test, y_train, y_test = train_test_split(data, class_labels, test_size=0.30, random_state=42)
#gnb.fit(X_train,np.ravel(y_train))
#print(y_train[1])
#data = np.asarray(data)
#data = data.tolist()
X_train = np.asarray(X_train)
X_train = X_train.tolist()
tr_sam = len(X_train)

y_train = np.asarray(y_train)
y_train = y_train.tolist()

classes = []

if len(classes) == 0:
    for i in range(0,n_clusters):
        classes.append([])

for i in range(0,len(y_train)):
    if y_train[i] == 0:
        classes[0].append(X_train[i])
    elif y_train[i] == 1:
        classes[1].append(X_train[i])
    elif y_train[i] == 2:
        classes[2].append(X_train[i])

print("class 0")
print(classes[0])

prob_class0 = len(classes[0]) / tr_sam
print("P(Class = 0) is ",prob_class0)

print("*****************************************************************")
print("class 1")
print(classes[1])

prob_class1 = len(classes[1]) / tr_sam
print("P(Class = 1) is ",prob_class1)

print("*****************************************************************")


#print(len(classes[0][0]))
def freq(buff):
    zeros = 0
    ones = 0
    for i in range(0,len(buff)):
        if buff[i] == 0:
            zeros = zeros+1
        elif buff[i] == 1:
            ones = ones+1
    return zeros,ones

prob_mat1 = [[]]

for k in range(0,len(classes[0][0])):
    buff = []
    for j in range(0,len(classes[0])):
        buff.append(classes[0][j][k])
    #print(buff)
    #print(np.asarray(buff))
    buff = np.asarray(buff)
    buff = np.reshape(buff,(-1,1))
    #print(len(buff))
    zeros,ones = freq(buff)
    prob_zeros_class0 = zeros/len(classes[0])
    prob_ones_class0 = ones/len(classes[0])
    if prob_mat1[0] == []:
        prob_mat1[0].append(prob_zeros_class0)
        prob_mat1[0].append(prob_ones_class0)
    else:
        l = len(prob_mat1)
prob_mat1.append([])
nl = l+1
prob_mat1[nl-1].append(prob_zeros_class0)
prob_mat1[nl-1].append(prob_ones_class0)

print("Probabilities of Class 0",prob_mat1)

prob_mat2 = [[]]

for k in range(0,len(classes[1][0])):
    buff = []
    for j in range(0,len(classes[1])):
        buff.append(classes[1][j][k])

    buff = np.asarray(buff)
    buff = np.reshape(buff,(-1,1))
    
    zeros,ones = freq(buff)
    prob_zeros_class1 = zeros/len(classes[1])
    prob_ones_class1 = ones/len(classes[1])
    if prob_mat2[0] == []:
        prob_mat2[0].append(prob_zeros_class1)
        prob_mat2[0].append(prob_ones_class1)
    else:
        l = len(prob_mat2)
prob_mat2.append([])
nl = l+1
prob_mat2[nl-1].append(prob_zeros_class1)
prob_mat2[nl-1].append(prob_ones_class1)

print("\nProbabilities of Class 1",prob_mat2)




print("\n Testing")
print("\n New Sample: 1,1,0,0,1,0")

samp = [1,1,0,0,1,0]

probofsam_class0 = 1
j = 0
for i in range(0,len(prob_mat1)):
    probofsam_class0 = prob_mat1[i][samp[j]] * probofsam_class0
    j = j+1

print("\nProbability of sample belonging to class: 0 is ",probofsam_class0)

probofsam_class1 = 1
j = 0
for i in range(0,len(prob_mat2)):
    probofsam_class1 = prob_mat2[i][samp[j]] * probofsam_class1
    j = j+1

print("\nProbability of sample belonging to class: 1 is ",probofsam_class1)





ch = max(probofsam_class0,probofsam_class1)
if ch==probofsam_class0:
    print("\n The given sample belongs to class: ",0)
elif ch==probofsam_class1:
    print("\n The given sample belongs to class: ",1)


# In[7]:


#Naive bayes
from __future__ import division, print_function
from sklearn.naive_bayes import GaussianNB,MultinomialNB

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import csv
import scikitplot as skplt
from sklearn import preprocessing

from pylab import scatter,show,plot
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score

from sklearn.metrics import precision_score,recall_score,accuracy_score


data = df

print('KMeans Labelling')
kmeans = KMeans(n_clusters=2).fit(data)
class_labels = kmeans.labels_

data2 = data
idx = 14
data2.insert(loc=idx, column = 'classs', value = class_labels)


#gnb = GaussianNB()
gnb = MultinomialNB()
X_train, X_test, y_train, y_test = train_test_split(data, class_labels, test_size=0.30, random_state=42)
gnb.fit(X_train,np.ravel(y_train))
y_pred= gnb.predict(X_test)

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    #print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

# Compute confusion matrix
cnf_matrix = confusion_matrix(y_pred,y_test)
np.set_printoptions(precision=2)

class_names = ['NO CHD','CHD']
# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix, without normalization')

plt.show()


target_names = ['class 1', 'class 2']
graph_cl = [1,2]
print('Naive Bayes Classifier Performance Metrics')
print(classification_report(y_test, y_pred, target_names=target_names))
precision = precision_score(y_test, y_pred, average=None)
print('Precision: ',precision)
recall = recall_score(y_test, y_pred, average=None)
print('Recall: ',recall)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy: ',accuracy)

plt.plot(graph_cl,precision,color='g')
plt.xlabel('Classes')
plt.ylabel('Precision')
plt.show()

plt.plot(graph_cl,recall,c='orange')
plt.xlabel('Classes')
plt.ylabel('Recall')
plt.show()


# In[5]:


#k-means
#elbow method
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
wcss=[]
for i in range (1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(df)
print(y_kmeans)

#visualisaion
plt.scatter(df[y_kmeans == 0],df[y_kmeans == 0],c = 'red', label = 'Cluster 1')
plt.scatter(df[y_kmeans == 1],df[y_kmeans == 1],c = 'blue', label = 'Cluster 2')


plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],  c = 'yellow', label = 'Centroids')
plt.title('Chd')
plt.legend()
plt.show()


# In[19]:


#k-means SSE plot
def drawSSEPlot(df, column_indices, n_clusters=8, max_iter=300, tol=1e-04, init='k-means++', n_init=10, algorithm='auto'): 
    import matplotlib.pyplot as plt
    inertia_values = []
    for i in range(1, n_clusters+1):
        km = KMeans(n_clusters=i, max_iter=max_iter, tol=tol, init=init, n_init=n_init, random_state=1, algorithm=algorithm)
        km.fit_predict(df.iloc[:, column_indices])
        inertia_values.append(km.inertia_)
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.plot(range(1, n_clusters+1), inertia_values, color='red')
    plt.xlabel('No. of Clusters', fontsize=15)
    plt.ylabel('SSE / Inertia', fontsize=15)
    plt.title('SSE / Inertia vs No. Of Clusters', fontsize=15)
    plt.grid()
    plt.show()
drawSSEPlot(df, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])


# In[4]:


#K-medoid
from sklearn_extra.cluster import KMedoids
from tqdm import tqdm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
data=df
df1= data[['totChol','sysBP','glucose','age']]

 


x=df1.drop('sysBP',1)
y=df1['totChol']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size =0.2, random_state=0)
no_clust= [1,2,3,4,5]
loss_values=[]
for i in tqdm(no_clust):
    k= KMedoids(n_clusters=i,init="k-medoids++")
    k.fit(x_train)
    loss_values.append(k.inertia_)
    labels = np.array(k.labels_)
    print("cluster labels along with frequency")
    print(np.unique(labels,return_counts=True))
    print("orginal distribution")
    print(np.unique(y_train,return_counts=True))
    print("#*50")
    
fig,ax=plt.subplots(figsize=(4,2))
plt.plot(range(1,len(no_clust)+1),loss_values,color='red',marker='o')
plt.xlabel('No. of clusters',fontsize=15)
plt.ylabel('SSE values',fontsize=15)
plt.title('SSE values vs No. of clusters',fontsize=15)
plt.grid()
plt.show()


# In[ ]:




