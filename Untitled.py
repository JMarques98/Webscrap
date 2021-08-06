#!/usr/bin/env python
# coding: utf-8

# In[11]:


from bs4 import BeautifulSoup


# In[12]:


import requests


# In[13]:


import pandas as pd


# In[14]:


url = 'https://coinmarketcap.com/es'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#CRYPTOCURRENCY 

cr = soup.find_all('p', class_ = 'sc-1eb5slv-0 iJjGCS')

crypto = list()

for i in cr: 
    crypto.append(i.text)


# In[15]:


#VALUE OF THE COIN

vl = soup.find_all('div', class_ = 'sc-131di3y-0 cLgOOr')

values = list()

for i in vl:
    values.append(i.text)


# In[16]:


#Save the Dataframe

df = pd.DataFrame({'Name': crypto, 'Value':values})
print(df)


# In[ ]:




