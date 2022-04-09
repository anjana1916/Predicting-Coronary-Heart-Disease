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

 

### Analytical:
1.	Which all factors can be considered as potential risk factors?  
2.	Why does males have high risk of getting CHD?  
3.	Show the records of the youngest and oldest age. What is the inference?  
4.	Can age be considered as a potential risk factor?  
5.	Why can’t BPMeds be taken as a potential risk factor?  
6.	Which age group is predominant?



