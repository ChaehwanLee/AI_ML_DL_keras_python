#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


file1 = pd.read_csv('/Users/LG/Desktop/실습1.csv')


# In[9]:


file2 = pd.read_csv('/Users/LG/Desktop/실습2.csv')


# In[10]:


실습3 = pd.concat([file1,file2])


# In[11]:


print(실습3)


# In[12]:


실습3


# In[ ]:




