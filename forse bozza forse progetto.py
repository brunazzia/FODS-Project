#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re


# In[ ]:





# In[2]:


trips= pd.read_csv(r'C:\Users\Utente\Downloads\metaData.csv')


# In[3]:


trips.columns


# In[4]:


# ztb.ds= pd.read_csv('https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/626723/ZTBus_compressed.zip?sequence=3&isAllowed=y')


# In[ ]:





# In[5]:


# arr = np.loadtxt("https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/626723/ZTBus_compressed.zip?sequence=3&isAllowed=y",
#                 delimiter=",", dtype=str)
#display(arr)


# In[6]:


trips


# 1. Extract all trips with busRoute 83

# In[7]:


trips.loc[trips['busRoute'] == '83']


# 2- Extract all trips where busRoute is not a number

# In[8]:


trips['busRoute'].dtype # prima risultava come int64, e per poter usare una regex serve che il tipo sia una stringa


# In[9]:


trips['busRoute1']= trips['busRoute'].astype(str)


# In[10]:


trips[trips['busRoute'].str.contains(r'\D')]


# 3. For each (busNumber, busRoute) pair, determine the number of trips

# In[11]:


# QUESTA SBAGLIATAtrips.groupby(trips['busNumber'])[['busRoute','busNumber']].count()


# In[12]:


busNumber= trips['busNumber'].drop_duplicates()
busRoute= trips['busRoute'].drop_duplicates()


# In[13]:


ds= tot= {}
for n in busNumber:
    tot[n]={}
    for r in busRoute:
        tot[n][r]= sum(trips[(trips['busNumber']==n) & (trips['busRoute']== r)]['busNumber'])
tot        


# 4. For each trip, compute the ratio between the energy consumption and the average number of passengers

# conversione in KiloJoules della colonna, per facilitare il calcolo

# In[15]:


trips['energyConsumption(KJ)']= trips['energyConsumption']/1000


# In[17]:


trips['ratio- KJ/Person']= trips['energyConsumption(KJ)']/trips['itcs_numberOfPassengers_mean']
trips['ratio- KJ/Person']= trips['ratio- KJ/Person'].astype(int)
trips.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




