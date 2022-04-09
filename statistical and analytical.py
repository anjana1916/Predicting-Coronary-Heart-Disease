#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import pandas
import pandas as pd
heart = pd.read_csv(r'E:\pdf files\logisticheart\framinghamcsv.csv')


# In[4]:


heart.head(10)


# In[4]:


heart.dtypes


# In[5]:


heart.columns


# In[9]:


x=input("enter the column : ")
print(heart[x].values.tolist())


# In[8]:


n = int(input("enter the record number to be viewed :"))
display(heart.iloc[n])


# In[5]:


heart.info()


# In[6]:


# age histogram analysis 
heart['age'].hist()


# In[7]:


#gender histogram analysis
heart['gender'].hist()


# In[9]:


# no: of cigarettes per day
heart['cigsPerDay'].hist()


# In[10]:


#total cholestrol level
heart['totChol'].hist()


# In[11]:


# systolic blood pressure
heart['sysBP'].hist()


# In[12]:


heart.hist()


# In[2]:


#boxplot of Total cholestrol
# Import libraries 
import matplotlib.pyplot as plt
fig = plt.figure(figsize =(10, 7))
plt.boxplot(heart['totChol'])


# In[14]:


#boxplot of systolic bloodpressure, diastolic bloodpressure, Body-mass index, heart rate
data = [heart['sysBP'],heart['diaBP'],heart['BMI'],heart['heartRate']]
plt.boxplot(data)


# In[15]:


#scatter plot of age Vs cigarettes smoked per day
plt.scatter(heart['age'],heart['cigsPerDay'])
plt.show()


# In[16]:


#line plot of age Vs cigarettes smoked per day
plt.plot(heart['age'],heart['cigsPerDay'])
plt.show()


# In[18]:


# import required modules 
import matplotlib.pyplot as plt 
from scipy import stats 


# assign data 
x = heart['age'] 
y = heart['totChol'] 


# linear regression 2017 data vs 2018 data 
slope, intercept, r, p, std_err = stats.linregress(x, y) 


# function to return slope 
def myfunc(x): 
	return slope * x + intercept 


mymodel = list(map(myfunc, x)) 

# scatter 
plt.scatter(x, y) 

# plotting the data 
plt.plot(x, mymodel) 

# display the figure 
plt.show() 


# In[3]:


# import required modules 
import matplotlib.pyplot as plt 
from scipy import stats 


# assign data 
x = heart['diaBP'] 
y = heart['sysBP'] 


# linear regression 
slope, intercept, r, p, std_err = stats.linregress(x, y) 


# function to return slope 
def myfunc(x): 
	return slope * x + intercept 


mymodel = list(map(myfunc, x)) 

# scatter 
plt.scatter(x, y) 

# plotting the data 
plt.plot(x, mymodel) 

# display the figure 
plt.show() 


# In[9]:


plt.scatter(heart["age"],heart["cigsPerDay"],color="blue",label="scatter")
 
plt.xlabel("age",color="green") #xlabel() defines the label of x-axis
plt.ylabel("cigsPerday",color="blue") #ylabel() defines the label of x-axis
plt.title("cigsperday vs age",color="green") #title() is used to give title of this scatter plot
 
plt.show()
plt.plot(heart["age"],heart["cigsPerDay"],color="red",label="line graph") #plot() is used to create line graph
plt.legend()


# In[27]:


data= heart.head(50)
plt.bar(data["age"],data["heartRate"],color=["green","blue","pink","red"])
 
plt.xlabel("age",color="green")
plt.ylabel("heartRate",color="blue")
plt.title("age Vs Heartrate",color="green")
plt.show()


# In[4]:


x=len(heart[heart.age<=35])  #people below 35 years of age
x1=len(heart[(heart.age>35) & (heart.age<55)])  #people above 35 and below 55 years of age
x2=len(heart[heart.age>=55])    #people above 55 years of age
 
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 
print(x,x1,x2)
plt.pie([x,x1,x2],colors=['yellow','red','blue'],labels=['less than or equal to 35','35-55','55 and above'],autopct='%1.0f%%')
 
plt.legend(title='Age')  # to shown the labels as legends
 
plt.show()


# In[71]:


x=len(heart[heart.gender==0])  #female
y=len(heart[heart.gender==1])    #male
 
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([x,y],colors=['yellow','red'],labels=['female','male'],autopct='%1.0f%%')
 
plt.legend(title='gender')  # to shown the labels as legends
 
plt.show()


# In[20]:


plt.bar(heart["age"],heart["heartRate"],color=["green","blue","pink","red"])
 
plt.xlabel("age",color="green")
plt.ylabel("heartRate",color="blue")
plt.title("age Vs Heartrate",color="green")
plt.show()


# In[11]:


x=len(heart[heart.TenYearCHD==0])  #no future risk of CHD
y=len(heart[heart.TenYearCHD==1])    #future risk of CHD
 
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal

print(x,y) 
plt.pie([x,y],colors=['yellow','blue'],labels=['no future risk of CHD','future risk of CHD'],autopct='%1.0f%%')
 
plt.legend(title='risk of CHD')  # to shown the labels as legends
 
plt.show()


# In[29]:


bins=[0,10,20,30,40,50,60,70,80,90,100,110,120]  #The bins are usually specified as consecutive, non-overlapping intervals of a variable.
 
#hist() is used to draw histogram
 
plt.hist(heart.age,bins,histtype='bar', rwidth=0.8) 
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('People')
plt.show()


# In[31]:


plt.bar(heart["age"],heart["BMI"],color=["green","blue","pink","red"])
 
plt.xlabel("age",color="green")
plt.ylabel("BMI",color="blue")
plt.title("age Vs BMI",color="green")
plt.show()


# In[32]:


plt.bar(heart["age"],heart["totChol"],color=["green","blue","pink","red"])
 
plt.xlabel("age",color="green")
plt.ylabel("total Cholestrol",color="blue")
plt.title("age Vs total Cholestrol",color="green")
plt.show()


# In[20]:



plt.bar(data["age"],data["TenYearCHD"],color=["green","blue","pink","red"])
 
plt.xlabel("age",color="green")
plt.ylabel("TenYearCHD",color="blue")
plt.title("age Vs TenYearCHD",color="green")
plt.show()


# In[63]:


lst1 = list(heart.gender)
lst2 = list(heart.TenYearCHD)
n= len(lst1)
x=x1=y=y1=0
for i in range(n):
    if lst1[i]==0 and lst2[i]==0:        #females who have no 10 year risk of CHD
        x=x+1
    elif lst1[i]==0 and lst2[i]==1:      #females who have 10 year risk of CHD
        x1=x1+1
    elif lst1[i]==1 and lst2[i]==0:      #males who have no 10 year risk of CHD
        y=y+1                           
    elif lst1[i]==1 and lst2[i]==1:      #males who have 10 year risk of CHD
        y1=y1+1

print(x,x1,y,y1)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 
#Here we need a list of values that are simply x,x1 and x2
#colors specify a list of colors in pie chart
#In order to specify labels we use labels attribute
 
plt.pie([x,x1,y,y1],colors=['yellow','red','blue','green'],labels=['females no CHD','females CHD','male no CHD','male CHD'])
 
plt.legend(title='Which gender has more risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2)

 
plt.show()


# In[57]:


len(heart.totChol)


# In[65]:


lst1 = list(heart.gender)
lst2 = list(heart.totChol)
n= len(lst1)
x=x1=y=y1=0
for i in range(n):
    if lst1[i]==0 and lst2[i]<=240:        #females with normal Cholesterol level
        x=x+1
    elif lst1[i]==0 and lst2[i]>240:      #females with higher Cholesterol level
        x1=x1+1
    elif lst1[i]==1 and lst2[i]<=240:      #males with normal Cholesterol level
        y=y+1                           
    elif lst1[i]==1 and lst2[i]>240:      #males with higher Cholesterol level
        y1=y1+1

print(x,x1,y,y1)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 
#Here we need a list of values that are simply x,x1 and x2
#colors specify a list of colors in pie chart
#In order to specify labels we use labels attribute
 
plt.pie([x,x1,y,y1],colors=['yellow','red','blue','green'],labels=['females normal Chol','females high Chol','male normal Chol','male high Chol'])
 
plt.legend(title='Which gender has more risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[74]:


x=len(heart[(heart.gender==0) & (heart.totChol<=240)])  
x1=len(heart[(heart.gender==0) & (heart.totChol>240)]) 
y=len(heart[(heart.gender==1) & (heart.totChol<=240)]) 
y1=len(heart[(heart.gender==1) & (heart.totChol>240)]) 

print(x,x1,y,y1)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([x,x1,y,y1],colors=['yellow','red','blue','green'],labels=['females normal Chol','females high Chol','male normal Chol','male high Chol'],autopct='%1.0f%%')
 
plt.legend(title='Which gender has more risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[12]:


x=len(heart[(heart.gender==0) & (heart.TenYearCHD==0)])  
x1=len(heart[(heart.gender==0) & (heart.TenYearCHD==1)]) 

print(x,x1)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([x,x1],colors=['lawngreen','indigo'],labels=['females no CHD','females CHD'],autopct='%1.0f%%')
 
plt.legend(title='Which gender has more risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[13]:


x=len(heart[(heart.gender==1) & (heart.TenYearCHD==0)])  
x1=len(heart[(heart.gender==1) & (heart.TenYearCHD==1)]) 

print(x,x1)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([x,x1],colors=['teal','aquamarine'],labels=['males no CHD','males CHD'],autopct='%1.0f%%')
 
plt.legend(title='Which gender has more risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[76]:


len(heart.cigsPerDay)


# In[78]:


x=len(heart[(heart.gender==0) & (heart.cigsPerDay==0)])  
x1=len(heart[(heart.gender==0) & (heart.cigsPerDay!=0)]) 


print(x,x1)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([x,x1],colors=['pink','red'],labels=['females no smoking','females smoking'],autopct='%1.0f%%')
 
plt.legend(title='Which gender has more risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[79]:


y=len(heart[(heart.gender==1) & (heart.cigsPerDay==0)]) 
y1=len(heart[(heart.gender==1) & (heart.cigsPerDay!=0)])
print(y,y1)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([y,y1],colors=['blue','green'],labels=['male no smoking','male smoking'],autopct='%1.0f%%')
 
plt.legend(title='Which gender has more risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[84]:


x=len(heart[(heart.TenYearCHD==1) & (heart.cigsPerDay==0)])  
x1=len(heart[(heart.TenYearCHD==1) & (heart.cigsPerDay!=0)]) 


print(x,x1)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([x,x1],colors=['SeaGreen','gold'],labels=['CHD but no smoking','CHD smoking'],autopct='%1.0f%%')
 
plt.legend(title='risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[8]:


heart[['TenYearCHD','gender']].describe()


# In[14]:


x=len(heart[(heart.TenYearCHD==1) & (heart.diabetes==0)])  
x1=len(heart[(heart.TenYearCHD==1) & (heart.diabetes==1)]) 


print(x,x1)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([x,x1],colors=['coral','crimson'],labels=['CHD but no diabetes','CHD diabetes'],autopct='%1.0f%%')
 
plt.legend(title='risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[16]:


x=len(heart[(heart.TenYearCHD==1) & (heart.sysBP<=120)])  
x1=len(heart[(heart.TenYearCHD==1) & (heart.sysBP>120) & (heart.sysBP<=129)])
y = len(heart[(heart.TenYearCHD==1) & (heart.sysBP>129)])


print(x,x1,y)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([x,x1,y],colors=['greenyellow','forestgreen','lightseagreen'],labels=['CHD normal sys.BP','elevated sys.BP','CHD high sys.BP'],autopct='%1.0f%%')
 
plt.legend(title='risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[17]:


x=len(heart[(heart.gender==1) & (heart.sysBP<=120)])  
x1=len(heart[(heart.gender==1) & (heart.sysBP>120) & (heart.sysBP<=129)])
y = len(heart[(heart.gender==1) & (heart.sysBP>129)])


print(x,x1,y)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([x,x1,y],colors=['cornflowerblue','royalblue','navy'],labels=['males normal sys.BP','males elevated sys.BP','males high sys.BP'],autopct='%1.0f%%')
 
plt.legend(title='risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[18]:


x=len(heart[(heart.gender==0) & (heart.sysBP<=120)])  
x1=len(heart[(heart.gender==0) & (heart.sysBP>120) & (heart.sysBP<=129)])
y = len(heart[(heart.gender==0) & (heart.sysBP>129)])


print(x,x1,y)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([x,x1,y],colors=['darkgoldenrod','goldenrod','gold'],labels=['females normal sys.BP','females elevated sys.BP','females high sys.BP'],autopct='%1.0f%%')
 
plt.legend(title='risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[5]:


heart[['age']].describe()


# In[11]:


x=heart[heart['age']==32].index.values
print(heart.iloc[2365,:])


# In[10]:


x=heart[heart['age']==70].index.values
print(heart.iloc[1624,:])
print(heart.iloc[3137,:])


# In[15]:


x=len(heart[(heart.TenYearCHD==1) & (heart.prevalentStroke==0)])  
x1=len(heart[(heart.TenYearCHD==1) & (heart.prevalentStroke==1)]) 


print(x,x1)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([x,x1],colors=['coral','crimson'],labels=['CHD but no prevalent stroke','CHD prevalent stroke'],autopct='%1.0f%%')
 
plt.legend(title='risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[14]:


x=len(heart[(heart.TenYearCHD==1) & (heart.prevalentHyp==0)])  
x1=len(heart[(heart.TenYearCHD==1) & (heart.prevalentHyp==1)]) 


print(x,x1)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([x,x1],colors=['coral','crimson'],labels=['CHD but no prevalent Hypertension','CHD prevalent Hypertension'],autopct='%1.0f%%')
 
plt.legend(title='risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[16]:


heart[['glucose']].describe()


# In[17]:


x=len(heart[(heart.TenYearCHD==1) & (heart.glucose<=140)])  
x1=len(heart[(heart.TenYearCHD==1) & (heart.glucose>140)]) 


print(x,x1)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([x,x1],colors=['coral','crimson'],labels=['CHD but normal glucose levels','CHD abnormal glucose levels'],autopct='%1.0f%%')
 
plt.legend(title='risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[21]:


x=len(heart[(heart.TenYearCHD==1) & (heart.prevalentStroke==0) & (heart.prevalentHyp==0) & (heart.glucose<=140) ])  
x1=len(heart[(heart.TenYearCHD==1) & (heart.prevalentStroke==1) & (heart.prevalentHyp==1) & (heart.glucose>140)])
x2 = len(heart[(heart.TenYearCHD==1) & (heart.prevalentStroke==1) & (heart.prevalentHyp==0) & (heart.glucose<=140) ]) 
x3 = len(heart[(heart.TenYearCHD==1) & (heart.prevalentStroke==1) & (heart.prevalentHyp==1) & (heart.glucose<=140) ]) 
x4 = len(heart[(heart.TenYearCHD==1) & (heart.prevalentStroke==0) & (heart.prevalentHyp==1) & (heart.glucose>140) ]) 
x5 = len(heart[(heart.TenYearCHD==1) & (heart.prevalentStroke==1) & (heart.prevalentHyp==0) & (heart.glucose>140) ])
x6 = len(heart[(heart.TenYearCHD==1) & (heart.prevalentStroke==1) & (heart.prevalentHyp==0) & (heart.glucose<=140) ])
x7 = len(heart[(heart.TenYearCHD==1) & (heart.prevalentStroke==0) & (heart.prevalentHyp==1) & (heart.glucose<=140) ])
x8 = len(heart[(heart.TenYearCHD==1) & (heart.prevalentStroke==0) & (heart.prevalentHyp==0) & (heart.glucose>140) ])
print(x,x1,x2,x3,x4,x5,x6,x7,x8)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([x,x1,x2,x3,x4,x5,x6,x7,x8],colors=['olive','yellow','lawngreen','gold','orange','khaki','moccasin','forestgreen','lime'],labels=['CHD no stroke,no Hyp,no glu','CHD stroke,Hyp,glu','CHD stroke','CHD stroke,Hyp,no glu','CHD no stroke,Hyp,glu','CHD stroke,no Hyp,glu','CHD stroke,no Hyp, no glu','CHD no stroke,Hyp,no glu','CHD no stroke,no Hyp,glu'],autopct='%1.0f%%')
 
plt.legend(title='risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[28]:


x=len(heart[(heart.age<=35) & (heart.TenYearCHD==1)])  
x1=len(heart[(heart.age>35) & (heart.age<55) & (heart.TenYearCHD==1)])  
x2=len(heart[(heart.age>=55) & (heart.TenYearCHD==1)])  
x3=len(heart[(heart.age<=35) & (heart.TenYearCHD==0)])  
x4=len(heart[(heart.age>35) & (heart.age<55) & (heart.TenYearCHD==0)])  
x5=len(heart[(heart.age>=55) & (heart.TenYearCHD==0)]) 
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 
print(x,x1,x2,x3,x4,x5)
plt.pie([x,x1,x2,x3,x4,x5],colors=['red','yellow','blue','lawngreen','pink','orange'],labels=['CHD less than or equal to 35',' CHD 35-55','CHD 55 and above','no CHD less than or equal to 35','no CHD 35-55','no CHD 55 and above'],autopct='%1.0f%%')
 
plt.legend(title='Age')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2)
plt.show()


# In[29]:


x=len(heart[(heart.TenYearCHD==1) & (heart.BPMeds==0)])  
x1=len(heart[(heart.TenYearCHD==1) & (heart.BPMeds==1)]) 


print(x,x1)
plt.axis('equal')  #for making pie chart circular,that makes major axis and minor axis equal
 

plt.pie([x,x1],colors=['lawngreen','blue'],labels=['CHD no BP meds','CHD BP meds'],autopct='%1.0f%%')
 
plt.legend(title='risk of getting CHD')  # to shown the labels as legends
plt.legend(loc="upper right", bbox_to_anchor=(0.5, 1.15), ncol=2) 
plt.show()


# In[2]:


heart[['totChol']].describe()


# In[3]:


heart[['sysBP']].describe()


# In[7]:


x=len(heart[(heart.gender==0)&(heart.BPMeds==1)])
y=len(heart[(heart.gender==0)&(heart.BPMeds==0)])
x1=len(heart[(heart.BPMeds==0)&(heart.gender==1)])
y1=len(heart[(heart.BPMeds==1)&(heart.gender==1)])
x,y,x1,y1


# In[4]:


import statistics
print(statistics.mode(heart['sysBP']))
print(statistics.mode(heart['totChol']))
print(statistics.mode(heart['age']))


# In[6]:


x=len(heart[(heart.prevalentStroke==0) & (heart.diabetes==0)])
y=len(heart[(heart.prevalentStroke==0) & (heart.diabetes==1)])
x1=len(heart[(heart.prevalentStroke==1) & (heart.diabetes==0)])
y1=len(heart[(heart.prevalentStroke==1) & (heart.diabetes==1)])
x,y,x1,y1


# In[ ]:


x=len(heart[(heart.prevalentStroke==0) & (heart.prevalentHyp==0)])
y=len(heart[(heart.prevalentStroke==0) & (heart.prevalentHyp==1)])
x1=len(heart[(heart.prevalentStroke==1) & (heart.prevalentHyp==0)])
y1=len(heart[(heart.prevalentStroke==1) & (heart.prevalentHyp==1)])
x,y,x1,y1

