
# coding: utf-8

# In[1]:

import nltk


# In[3]:

nltk.app


# In[4]:

from nltk.book import *


# In[5]:

text1


# In[6]:

text2


# In[7]:

text1.concordance("monstrous")


# In[8]:

text2.concordance("affection")


# In[9]:

text3.concordance("lived")


# In[10]:

text1.similar("monstrous")


# In[11]:

text4.dispersion_plot(["citizens","democracy","freedom","duties","America"])


# In[12]:

text3.generate()


# In[13]:

text3


# In[14]:

len(text3)


# In[15]:

sorted(set(text3))


# In[16]:

len(set(text3))


# In[17]:

text3.count("smote")


# In[18]:

tex3.count("is")


# In[19]:

text3.count("is")


# In[20]:

def lexical_diversity(text):
    return len(text)/len(set(text))


# In[21]:

def percentage(count):
    return 100 * count / total


# In[22]:

lexical_diversity(text3)


# In[23]:

lexical_diversity(text7)


# In[24]:

sent1 = ["call","me","shubham","."]


# In[25]:

sent1


# In[26]:

len(sent1)


# In[27]:

##indexing the list
text4[172]


# In[28]:

text4.index('awaken')


# In[29]:

text4.index('to')


# In[30]:

text5[16715:16735]


# In[31]:

##yoon hi
name = "shubham"
name *2


# In[32]:

V = set(text1)
long_words = [w for w in V if len(w) > 15]


# In[33]:

sorted(long_words)


# In[35]:

fdist = FreqDist(text5)
sorted([w for w in set(text5) is len(w) > 7 and fdist5[w] >7])


# In[36]:

bigrams(['more','is','said','than','done'])


# In[37]:

nltk.bigrams()


# In[38]:

text4.collocations()


# In[39]:

babelize_shell()


# In[ ]:



