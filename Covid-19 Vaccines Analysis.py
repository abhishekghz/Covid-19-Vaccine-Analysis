#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("country_wise_latest.csv")
data.head()


# In[3]:


data.describe()


# In[4]:


data = pd.read_csv("covid_19_clean_complete.csv")
data.head()


# In[5]:


data = pd.read_csv("day_wise.csv")
data.head()


# In[6]:


data = pd.read_csv("full_grouped.csv")
data.head()


# In[7]:


data = pd.read_csv("usa_county_wise.csv")
data.head()


# In[15]:


data = pd.read_csv("country_vaccinations.csv")
data.head()


# In[17]:


data = data[data.country.apply(lambda x: x not in ["England", "Scotland", "Wales", "Northern Ireland"])]
data.country.value_counts()


# In[18]:


data.vaccines.value_counts()


# In[19]:


df = data[["vaccines", "country"]]
df.head()


# In[20]:


dict_ = {}
for i in df.vaccines.unique():
  dict_[i] = [df["country"][j] for j in df[df["vaccines"]==i].index]

vaccines = {}
for key, value in dict_.items():
  vaccines[key] = set(value)
for i, j in vaccines.items():
  print(f"{i}:>>{j}")


# In[24]:


import plotly.express as px
import plotly.offline as py


vaccine_map = px.choropleth(data, locations = 'iso_code', color = 'vaccines')
vaccine_map.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
vaccine_map.show()


# In[ ]:




