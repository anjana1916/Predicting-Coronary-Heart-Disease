# **Predicting-Coronary-Heart-Disease**  
This data is taken from Kaggle website, it is based on an ongoing cardiovascular study on residents of the town of Framingham, Massachusetts. There are two classes – patients having ten year risk of future coronary heart disease (CHD) and the patients not having ten year risk of future CHD. The dataset provides the patient’s medical history. It includes over 4,000 records and 16 attributes.
### Attributes:
#### Demographic:
• Sex: male or female  
• Age: Age of the patient
#### Behavioral
• Current Smoker: whether or not the patient is a current smoker   
• Cigs Per Day: the number of cigarettes that the person smoked on average in one day. 
#### Medical( history)
• BP Meds: whether or not the patient was on blood pressure medication   
• Prevalent Stroke: whether or not the patient had previously had a stroke   
• Prevalent Hyp: whether or not the patient was hypertensive   
• Diabetes: whether or not the patient had diabetes 
#### Medical(current)
• Tot Chol: total cholesterol level   
• Sys BP: systolic blood pressure   
• Dia BP: diastolic blood pressure   
• BMI: Body Mass Index   
• Heart Rate: heart rate   
• Glucose: glucose level 
#### Predict variable (desired target)
• 10 year risk of coronary heart disease CHD 

![dataset](https://user-images.githubusercontent.com/103304121/162565285-c1ed041f-86ca-4adc-8524-fff28881da82.png)
![dataset1](https://user-images.githubusercontent.com/103304121/162565287-73acd23b-87ca-4288-a200-d960f29e7583.png)
![dataset22](https://user-images.githubusercontent.com/103304121/162565441-f2433711-99c2-44a2-9593-b6415eac6587.png)  

### Class level Details:
Provide details about how many classes are there in the dataset
              There are two classes – patients having ten-year risk of future coronary heart disease (CHD) and the patients not having ten-year risk of future CHD.  
Why Data Mining is required for this dataset?  
Data mining is basically used to extract useful information from raw dataset. The dataset I have chosen is taken from Kaggle website, it is based on an ongoing cardiovascular study on residents of the town of Framingham, Massachusetts. There are two classes – patients having ten-year risk of future coronary heart disease (CHD) and the patients not having ten-year risk of future CHD. The dataset provides the patient’s medical history. It includes over 4,000 records and 15 attributes. 
            The early prognosis of cardiovascular diseases can aid in making decisions on lifestyle changes in high-risk patients and in turn reduce the complications. In this study we intend to highlight the most relevant risk factors of heart disease as well as predict the overall risk using data mining techniques. Since our target variable is categorical or Boolean, we use Logistic regression in this study.  

### Objective
  In this study we are going to check if factors like – Total cholesterol levels, gender, age, Blood pressure levels, glucose levels, cigarettes smoked per day etc.. are potential risk factors of Coronary heart disease by answering few statistical and analytical questions.
    
#### Statistical:  
1.	Which is the average number of males and females in your dataset?  
Females = 0.57 and males = 0.43
That is 57% of the patients in our dataset are females and 43% are males.
![s1](https://user-images.githubusercontent.com/103304121/162566853-ffce1cdf-cac9-414c-82ac-ce059d86a69b.png)
 
2.	What is the maximum and minimum levels of total Cholesterol?  
![s2](https://user-images.githubusercontent.com/103304121/162566879-687fbb4c-2cbf-4587-be14-cbc47ed673a1.png)  
![s22](https://user-images.githubusercontent.com/103304121/162566902-bd056225-ad97-46a6-ab72-b589df04ec37.png)  
Range = max – min = 696 – 107 = 589
From this we can observe that the cholesterol levels is going as high as 696 which is not normal. And the average is coming close to 240 (greater than 240 is not normal levels). Most frequently occurring Total Cholesterol level is 220, which falls under normal category.
  
3.	What is the average systolic blood pressure?  
![s3](https://user-images.githubusercontent.com/103304121/162566927-da1294c5-a8c9-431d-9e95-8ac09a4a9474.png)
![s33](https://user-images.githubusercontent.com/103304121/162566943-73eae993-3823-48d4-b6a9-b17d49be8d7d.png)  
From this we can observe that the average is exceeding normal systolic blood pressure levels that is 120. Therefore there are patients with elevated and high blood pressure levels. Most frequently occurring systolic Blood pressure level is 120
  
4.	What is the average number of the total patients having ten-year risk of getting Coronary heart disease?  
![s4](https://user-images.githubusercontent.com/103304121/162566969-205947af-55a3-49c8-8a19-551e4c50fbeb.png)
No risk of CHD = 0.85     risk of CHD = 0.15
85% of the patients in our dataset have no risk of CHD while the remaining 15% has a risk of getting CHD.
 
5.	What is the average number of males and females having future risk of CHD?  
 ![s5](https://user-images.githubusercontent.com/103304121/162567016-6c27c98c-7ac3-4be5-915e-fc5bbe277ec9.png)
 If we look at females alone, the average number of females having future risk of coronary heart disease is 0.12 (301 out of 2419 females) that is 12% of the total population of females.  
 ![s55](https://user-images.githubusercontent.com/103304121/162567030-d5160a1d-4192-4bf3-8ffd-6382a9ba248b.png)
If we look at Males alone, the average number of males having coronary heart disease is 0.19 (343 out of 1819 males) that is 19% of the total population of males.
![s555](https://user-images.githubusercontent.com/103304121/162567170-c5c11219-a7b1-416f-8866-407f5d2b736e.png)


6.	What is the youngest and oldest patient?  
![s6](https://user-images.githubusercontent.com/103304121/162567143-e0b2814f-d328-4166-b6d4-e95ed465f247.png)
![s66](https://user-images.githubusercontent.com/103304121/162567150-d5b58c23-c512-4e67-b204-b78c9ac8c915.png)  
Range = max – min = 38
From this we can observe that the oldest patient is 70 years old and the youngest patient is 32 years old. Most frequently occurring age is 40.

 

#### Analytical:
1.	Which all factors can be considered as potential risk factors?  
2.	Why does males have high risk of getting CHD?  
In our dataset we have 15 factors taken from demographic, behavioural and medical records of each patient. We will have to go through all the risk factors and narrow it down to a few important potential risk factors.   

Cigarettes smoked per day: Risk of future CHD due to smoking
![a1](https://user-images.githubusercontent.com/103304121/162567455-73faef3c-a50d-4857-b461-9ead073b6e42.png)
![a11](https://user-images.githubusercontent.com/103304121/162567458-cdea4246-9d1b-4918-acd3-f12b0c70f642.png)
![a12](https://user-images.githubusercontent.com/103304121/162567459-f6028ac4-572d-40bf-85d3-b5c19c133640.png)  

From the Pie chart we can take cigarette smoking as a potential risk factor. As you can 52% of the population who have CHD risk are smokers. And when I classify his category again with respect to gender we can see that 61% of the male population are smokers which is more that half. This could be one reason for high risk of CHD in males.    
Diabetes:   
![a13](https://user-images.githubusercontent.com/103304121/162567461-ec9da9bd-f8f1-427d-bfb4-6e2e7c7f62d8.png)  
In the pie chart you can see that 94% of the population who have a risk of CHD has no diabetes. Therefore this factor is not as reliable as the previous one and is ruled out.

Systolic Blood Pressure:   
![a14](https://user-images.githubusercontent.com/103304121/162567462-21f5edab-7ce4-4cb9-985e-eeaaf8d7c009.png)  
From the pie chart we can see that 66% of the population having CHD has high systolic blood pressure and 16% have elevated systolic blood pressure. Therefore systolic blood pressure can be considered as a potential risk factor.  

Taking factors like – Prevalent stroke, Prevalent Hypertension and Glucose levels  
![a15](https://user-images.githubusercontent.com/103304121/162567463-030788cd-25ea-44c1-b073-1b7023b3c482.png)
![a16](https://user-images.githubusercontent.com/103304121/162567464-fd94236a-1507-487b-a659-8f4dcfb62de4.png)
![a17](https://user-images.githubusercontent.com/103304121/162567465-d8707e43-4aec-40fa-97b3-f11594677a70.png)

These 3 factors taken individually is not a reliable risk factor. But taken in a combination can act as a potential risk factor.  This is shown below,  
![a18](https://user-images.githubusercontent.com/103304121/162567467-086acb62-38ee-46f8-9984-d01d1cec1cca.png)

  
3.	Show the records of the youngest and oldest age. What is the inference?  
![a3](https://user-images.githubusercontent.com/103304121/162567611-ba0d1222-5ba2-4ca0-9684-1562d84b6df0.png) 
![a33](https://user-images.githubusercontent.com/103304121/162567620-279f63ef-eb8e-4242-a297-f23b3b1a14ad.png)  
From the two age categories – The youngest(32 years) has normal total cholesterol level and systolic blood pressure, but is a smoker. His medical history shows  no prevalent stroke or hypertension, which is probably the reason why it is showing no future risk.
There are two 70 year olds. The first patient has normal cholesterol levels and blood pressure and is not a smoker, but medical history shows prevalent stroke and hypertension which is probably the reason why it is showing there is a risk of CHD.
The second patient has normal cholesterol levels and systolic bloode pressure, has prevalent Hypertension but it is showing no risk of CHD
 
4.	Can age be considered as a potential risk factor?  
From the Pie chart we can infer that the factor age cannot be ignored. It is also taken as a potential Risk factor.  
![a4](https://user-images.githubusercontent.com/103304121/162567653-5100cf77-3261-4a66-868d-3aada773e720.png)
  
5.	Why can’t BPMeds be taken as a potential risk factor?  
![a5](https://user-images.githubusercontent.com/103304121/162567689-49cb1cce-0598-4dc7-8bed-bea2c1b9f2d6.png)  
From this Pie-chart we can infer that it is not a potential risk factor since more than ¾ th of the population having CHD does not take Blood pressure medicine. Therefore it is not a reliable factor. 
  
6.	Which age group is predominant?  
![a6](https://user-images.githubusercontent.com/103304121/162567708-7e7c9329-0298-44fe-b3c1-465254ad204d.png)  
From the pie-chart we can see that majority of the patients are from the age group 35-55, with an average of 0.67.
Other age groups include: less than 35 = 0.02, 55 and above = 0.31  

### Exploratory Data Analysis:
●	To take a closer look at the data took help of “ .head()”function of pandas library which returns first five observations of the data set. Similarly “.tail()” returns last five observations of the data set.  
![1](https://user-images.githubusercontent.com/103304121/162574896-8328375a-d6bd-40bf-a5b5-b44b9a696032.png)    

●	I found out the total number of rows and columns in the data set using “.shape”.  
![2](https://user-images.githubusercontent.com/103304121/162574909-7b472f69-d180-4f6c-aa05-5d7eca9f0bd0.png)  

●	Dataset comprises of 4238 observations and 15 characteristics.  
●	Out of which one is dependent variable and rest 14 are independent variables — medical characteristics.  
●	Columns and their corresponding data types,along with finding whether they contain null values or not. In my dataset there are null values in few columns, namely: totChol, BMI, heartrate, and glucose.  
The datatypes for categorical attributes are also wrong, it is saved as integers. This can be rectified in cleaning process.  
![3](https://user-images.githubusercontent.com/103304121/162574936-dec4ab61-e9a9-4212-a0df-83b8bf761263.png)  

 
●	The describe() function in pandas is very handy in getting various summary statistics.This function returns the count, mean, standard deviation, minimum and maximum values and the quantiles of the data.  
![4](https://user-images.githubusercontent.com/103304121/162574948-00775438-8050-4256-a44b-eea623d15836.png)  

 
From the above image you can see that there is a huge difference between Q3 and maximum value in two columns – totChol and glucose, which suggests that there might be outliers.
And in most of the columns mean is greater than the median which means the data is skewed to the right.  
●	Target variable/Dependent variable is discrete and categorical in nature.  
![5](https://user-images.githubusercontent.com/103304121/162574976-c65144bc-38db-4163-b3fd-5cc7a8be34da.png)

 
2 categories 0 and 1 – No CHD and CHD  
●	This tells us the count of each category in descending order.  
![6](https://user-images.githubusercontent.com/103304121/162574986-082df36b-2c27-47bb-b957-d7857b7c6d32.png)  

Here we have mode of each numerical columns,  
![8](https://user-images.githubusercontent.com/103304121/162575040-e86b0a7b-9060-4e99-936b-9a3beda7bf21.png)  

The attributes age, cigsperday, sysBP, diaBP, glucose have mode less than its mean, therefore the distribution is skewed to the right. For totChol the mode is greater than mean, therefore its skewed to the left. For heartrate mean, median and mode is almost aligned. 





