#!/usr/bin/env python
# coding: utf-8

# # EDA and Stock Analysis With Time Series Data of Tesala
# 

# In[1]:


get_ipython().system('pip install pandas.datareader')


# In[2]:


import pandas_datareader as pdr
import pandas as pd
from datetime import datetime


# In[3]:


tesla=pdr.get_data_yahoo('TSLA')


# In[4]:


type(tesla)


# In[5]:


tesla.tail()


# In[6]:


tesla.shape


# In[7]:


tesla.plot(figsize=(12,4))


# In[8]:


tesla['High'].plot(figsize=(12,4))


# In[9]:


## x limt and y limt
tesla['High'].plot(xlim=['2022-02-28','2020-09-01'],ylim=[0,900],figsize=(12,4))


# In[10]:


## x limt and y limt and colouring
tesla['High'].plot(xlim=['2020-01-01','2020-09-01'],ylim=[0,900],figsize=(12,4),ls='--',c='#F1C40F')


# In[11]:


index=tesla.iloc[0:4].index


# In[12]:


index


# In[13]:


index=tesla.loc['2022-02-28':'2022-03-03'].index


# ### Share open at 

# In[14]:


share_open=tesla.loc['2022-02-28':'2022-03-03']['Open']
share_open


# In[15]:


index=tesla.index
index


# In[16]:


import matplotlib as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


#figure,axis=plt.subplots()
#plt.tight_layout()
#figure.autofmt_xdate()
#axis.plot(index,share_open)


# ### reating the index

# In[18]:


tesla.reset_index(inplace=True)


# In[97]:


tesla.set_index("Date")


# ### To convert the object to date format

# In[98]:


pd.to_datetime(tesla['Date'])


# In[107]:


datetime.now()


# In[105]:


from datetime import datetime


# ## Time Resampling

# yntax : DataFrame.resample(rule, how=None, axis=0, fill_method=None, closed=None, label=None, convention=’start’, kind=None,            loffset=None, limit=None, base=0, on=None, level=None)
# 
# Parameters :
# 
# rule : the offset string or object representing target conversion
# 
# axis : int, optional, default 0
# 
# closed : {‘right’, ‘left’}
# 
# label : {‘right’, ‘left’}
# 
# convention : For PeriodIndex only, controls whether to use the start or end of rule
# 
# loffset : Adjust the resampled time labels
# 
# base : For frequencies that evenly subdivide 1 day, the “origin” of the aggregated intervals. For example, for ‘5min’ frequency, base could range from 0 through 4. Defaults to 0.
# 
# on : For a DataFrame, column to use instead of index for resampling. Column must be datetime-like.
# 
# level : For a MultiIndex, level (name or number) to use for resampling. Level must be datetime-like.

# In[27]:


tesla=tesla.set_index(tesla['Date'])


# In[24]:


tesla


# In[26]:


tesla.resample(rule='A')


# Resampling generates a unique sampling distribution on the basis of the actual data. We can apply various frequency to resample our time series data. This is a very important technique in the field of analytics.
# 
# Most commonly used time series frequency are –
# 
# W : weekly frequency
#     
# M : month end frequency
#     
# SM : semi-month end frequency (15th and end of month)
#     
# Q : quarter end frequency

# In[36]:


# Resampling the time series data based on months
# we apply it on stock close price
# 'M' indicates month
monthly_resampled_data = tesla.resample('M').mean() ['Close'].plot(figsize=(12,4),c='#C943D9')


#  the above command will find the mean closing price
#  of each month for a duration of 12 months.

# In[42]:


tesla.resample(rule='A').max() ['Open'].plot(figsize=(12,4),c='#C943D5')


# In[47]:


weekly_resampled_data = tesla.resample('W').mean() ['Open']
weekly_resampled_data
 
# find the mean opening price of tesla of each week for each week over a period of 1 year.


# In[49]:


weekly_resampled_data = tesla.resample('W').mean() ['Open'].plot(figsize=(12,4),c='#10F633')


# In[53]:


Quater_resampled_data = tesla.resample('Q').mean() ['Open'].plot(figsize=(12,4),c='#F61433')


# mean opening price of tesla of each quarter over a period of 1 year.

# In[57]:


Quater_resampled_data = tesla.resample('Q').mean() ['Open'].plot(kind='bar',figsize=(12,4),color='#F61433')


# ## Rolling

# In[65]:


tesla['High'].rolling(2).sum()


# In[63]:


tesla['High'].head()


# In[68]:


tesla['Open:10 days rolling']=tesla['Open'].rolling(10).mean()


# In[70]:


tesla.head(11)


# In[74]:


tesla[['Open','Open:10 days rolling']].plot(figsize=(18,8))

