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

#CRIPTOMONEDA 

cr = soup.find_all('p', class_ = 'sc-1eb5slv-0 iJjGCS')

criptomonedas = list()

for i in cr: 
    criptomonedas.append(i.text)


# In[15]:


#VALOR 

vl = soup.find_all('div', class_ = 'sc-131di3y-0 cLgOOr')

valores = list()

for i in vl:
    valores.append(i.text)


# In[16]:


#Se guarda en un dataframe

df = pd.DataFrame({'Name': criptomonedas, 'Value':valores})
print(df)


# In[ ]:




