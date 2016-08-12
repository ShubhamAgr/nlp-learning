
# coding: utf-8

# In[1]:

import nltk


# In[2]:

nltk.corpus.gutenberg.fileids()


# In[3]:

emma = nltk.corpus.gutenberg.words('austen-emma.txt')


# In[4]:

len(emma)


# In[5]:

emma.concordance("is")


# In[6]:

emma.concordance("surprize")


# In[7]:

from nltk.corpus import gutenberg


# In[8]:

gutenberg.fileids()


# In[9]:

for fileid in gutenberg.fileids():
    num_char = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))


# In[12]:

print(int(num_char/num_words),int(num_words/num_sents),int(num_words/num_vocab),fileid)


# In[13]:

macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')


# In[14]:

macbeth_sentences


# In[15]:

macbeth_sentences[1037]


# In[16]:

longest_len = max([len(s) for s in macbeth_sentences])


# In[17]:

[s for s in macbeth_sentences if len(s) == longest_len]


# In[19]:

from nltk.corpus import wordnet


# In[20]:

from nltk.corpus import wordnet as wn


# In[48]:

wn.synsets('fuck')


# In[49]:

print(wn.synset('fuck.n.01').lemma_names())
print(wn.synset('fuck.n.01').definition())
print(wn.synset('fuck.n.01').examples())

