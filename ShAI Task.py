#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt


# In[10]:


#Import Data 
Da=pd.read_csv(r'C:\Users\a\Desktop\Salaries.csv')
Da


# In[ ]:





# In[18]:


Da.shape
Da.info() 
Da.isnull()
Da.isnull().sum()


# In[76]:


Da.describe() 
range_salaries= 74768.321972 #The Mean value for TotalPay is The Range of Salaries
std_salaries = 50517.005274
Da.describe() 


# In[42]:


# fill missing values with mean column values
Da.fillna(Da.mean(), inplace=True)
# count the number of NaN values in each column
print(Da.isnull().sum())


# In[ ]:


Da.hist(figsize=(20,15))
plt.show()


# In[85]:


# Plotting a basic histogram
plt.hist(Da['TotalPayBenefits'], bins=30, color='skyblue', edgecolor='black')


# In[72]:


job=Da.groupby('JobTitle')
job.first()
job.describe()


# In[78]:


cor=Da.corr()
cor

sns.heatmap(cor.rank(axis='columns'),annot=True,fmt='.1f',linewidth=0.5)


# In[87]:


Da.scatter=('TotalPayBenefits','Benefits')
plt.show()


# In[88]:


Da.hist(figsize=(20,15))
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




