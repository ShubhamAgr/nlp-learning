
# coding: utf-8

# In[2]:

import nltk,re , pprint
from nltk import word_tokenize


# In[5]:

from urllib import request


# In[6]:

url = "http://www.gutenberg.org/files/2554/2554.txt"


# In[23]:

response = request.urlopen(url)
print(response)


# In[24]:

raw = response.read().decode('utf8')


# In[25]:

print(raw)


# In[26]:

type(raw)


# In[27]:

len(raw)


# In[28]:

raw[:75]


# In[29]:

tokens = word_tokenize(raw)


# In[30]:

type(tokens)


# In[31]:

len(tokens)


# In[32]:

tokens[:10]


# In[33]:

text = nltk.Text(tokens)


# In[34]:

type(text)


# In[35]:

text[1024:1062]


# In[36]:

text.collocations()


# In[37]:

raw.find("PART I")


# In[51]:

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = request.urlopen(url).read().decode('utf8')
html[:60]


# In[52]:

from bs4 import BeautifulSoup as bs
raw = bs(html,"lxml").get_text()
tokens = word_tokenize(raw)
tokens


# In[48]:

tokens = tokens[110:390]
text = nltk.Text(tokens)
text.concordance('gene')


# In[ ]:



