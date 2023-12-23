#!/usr/bin/env python
# coding: utf-8

# Red Wine Quality Prediction Project

# In[102]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn import  preprocessing



# Project Description
# The dataset is related to red and white variants of the Portuguese "Vinho Verde" wine. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).
# 
# This dataset can be viewed as classification task. The classes are ordered and not balanced (e.g. there are many more normal wines than excellent or poor ones). Also, we are not sure if all input variables are relevant. So it could be interesting to test feature selection methods.
# 

# In[103]:


df=pd.read_csv("https://raw.githubusercontent.com/FlipRoboTechnologies/ML-Datasets/main/Red%20Wine/winequality-red.csv")
df


# In[104]:


df.head(15)


# In[105]:


df.tail(30)


# In[106]:


df.shape


# In[107]:


df.columns


# In[108]:


df.columns.tolist()


# In[109]:


df.dtypes


# In[110]:


df.isnull().sum()


# In[111]:


df.info()


# In[112]:


for i in df.columns:
    print(df[i].value_counts())
    print("\n")


# In[113]:


df["quality"]=df["quality"].replace(" ",np.nan)
df["quality"].value_counts()


# In[114]:


df.iloc[480:500,:]


# In[115]:


df.isnull().sum()


# In[116]:


df['good'] = [1 if q >= 7 else 0 for q in df['quality']]


# In[117]:


df


# In[118]:


df.describe()


# In[119]:


from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report


# In[120]:


scaler = StandardScaler()
X = scaler.fit_transform(X)


# Data Visualization

# In[121]:


ax=sns.countplot(x = "quality",data=df)
print(df["quality"].value_counts())


# In[122]:


#check the skewnwss
df.skew()


# In[123]:


cor =df.corr()
cor


# In[124]:


plt.figure(figsize=(20,15))
plt.figure(figsize=(20,15))
sns.heatmap(df.corr(),linewidths= 0.1, fmt="1g",linecolor="Black",annot=True, cmap="Blues_r")
plt.yticks(rotation=0);
plt.show()


# In[125]:


X = df.iloc[:,:-2]   # exclude 'quality' and 'good' columns
y = df['good']


# In[126]:


X


# In[127]:


y


# In[128]:


X_train.shape


# In[129]:


X_train, X_test,y_train,y_test =train_test_split(X,y, test_size=0.3,random_state=42)


# In[130]:


dtc=DecisionTreeClassifier()


# In[131]:


dtc.fit(X_train,y_train)


# In[132]:


#Scale the data
min_max_scaler = preprocessing.MinMaxScaler()
X_train_scaled = min_max_scaler.fit_transform(X_train)
X_test_scaled = min_max_scaler.transform(X_test)


# In[133]:


X_train_scaled


# In[134]:


X_test_scaled


# In[135]:


#feature selection
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
selector = SelectKBest(f_classif, k=5)
X_train_new = selector.fit_transform(X_train_scaled, y_train)
X_test_new = selector.transform(X_test_scaled)
selected_features = X.columns[selector.get_support()]
print(selected_features)


# In[136]:


#train the decision tree classifier
dtc = DecisionTreeClassifier(random_state=42)
dtc.fit(X_train_new, y_train)


# In[137]:


y_pred = dtc.predict(X_test_new)


# In[138]:


y_pred


# In[139]:


#Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)


# In[140]:


#Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)


# Hyper Parameter Tuning

# In[141]:


#ROC AUC
roc_auc = roc_auc_score(y_test, dtc.predict_proba(X_test_new)[:,1])
print('ROC AUC:', roc_auc)


# In[143]:


import pickle

# replace DecisionTreeClassifier with the chosen model class
dtc = DecisionTreeClassifier(random_state=42)
dtc.fit(X_train, y_train)

# save model to a file using pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model,f) 
#saved the model from file                
with open('model.pkl', 'rb') as f:
    dtc= pickle.load(f)


# In[ ]:




