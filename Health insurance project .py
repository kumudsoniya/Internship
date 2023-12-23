#!/usr/bin/env python
# coding: utf-8

# In[71]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pickle


# In[72]:


df=pd.read_csv("https://raw.githubusercontent.com/FlipRoboTechnologies/ML-Datasets/main/Medical%20Cost%20Insurance/medical_cost_insurance.csv")


# In[47]:


df


# In[48]:


df.shape


# In[49]:


df.head()


# In[50]:


df.tail()


# In[51]:


df.dtypes


# In[52]:


df.isnull().sum()


# In[53]:


df.nunique().to_frame("No of unique values")


# In[54]:


#checking the value of counts in each column
for i in df.columns:
    print(df[i].value_counts())
    print("\n")
    


# In[55]:


print("total duplicate rows are",df.duplicated().sum())


# In[56]:


duplicate_rows=df[df.duplicated()]
print(duplicate_rows)


# In[57]:


unique_rows=df[~df.duplicated()]
print(unique_rows)


# In[58]:


df.head()


# In[59]:


df.tail()


# In[60]:


df.shape


# In[61]:


#decription of dataset
df.describe()


# In[63]:


#Encode categorical variables (if any)
df = pd.get_dummies(df, columns=['sex', 'smoker', 'region'])


# In[80]:


X = df.drop('charges', axis=1)  # independent variables
y = df['charges']


# In[81]:


df.head()


# In[84]:


sns.lmplot(x= "charges",y ="bmi",data=df,palette="colorblind")


# In[87]:


sns.lmplot(x= "charges",y ="age",data=df,palette="colorblind")


# In[88]:


sns.lmplot(x= "charges",y ="children",data=df,palette="colorblind")


# In[90]:


df.corr()


# In[66]:


# Split your data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)



# In[68]:


#Define a Linear Regression model and train it on the training data
reg = LinearRegression()
reg.fit(X_train, y_train)


# In[69]:


#predictions on the testing data
y_pred = reg.predict(X_test)



# In[73]:


#model on the testing data
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print("RMSE:", rmse)
print("R-squared score:", r2)


# In[91]:


#Save the final model 
filename = 'health_insurance_model.pkl'
pickle.dump(reg, open(filename, 'wb'))


# In[ ]:




