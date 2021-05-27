#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
movies=pd.read_csv('http://bit.ly/imdbratings')
movies


# In[2]:


movies.describe()


# In[4]:


movies.shape


# In[5]:


movies.dtypes


# In[6]:


type(movies)


# In[7]:


movies.describe(include=['object'])


# In[8]:


movies['title'].sort_values(ascending=False)


# In[9]:


movies.sort_values('title',ascending=False)


# In[10]:


movies.sort_values(['title','genre'],ascending=True)


# In[11]:


movies.head()


# In[13]:


booleans=[]
for length in movies.duration:
    if length >=200:
        booleans.append(True)
    else:
        booleans.append(False)
    


# In[17]:


len(booleans)


# In[18]:


is_long=pd.Series(booleans)
is_long


# In[19]:


movies[is_long]


# In[20]:


is_long= movies.duration >=200
is_long


# In[21]:


movies[is_long]


# In[22]:


movies[movies.duration >=200]


# In[23]:


movies[movies.duration >=200].genre


# In[24]:


movies[(movies.duration >=200) | (movies.genre== 'Drama')]


# In[25]:


movies[(movies.duration >=200) & (movies.genre== 'Drama')]


# In[26]:


(movies.duration >=200) & (movies.genre== 'Drama')


# In[27]:


movies[movies.genre.isin(['Crime','Drama','Action'])]


# In[28]:


movies.genre.describe()


# In[29]:


movies.genre.value_counts()


# In[30]:


movies.genre.unique()


# In[31]:


movies.genre.nunique()


# In[33]:


pd.crosstab(movies.genre,movies.content_rating)


# In[34]:


movies.duration.describe()


# In[36]:


movies.duration.mean()


# In[37]:


movies.duration.value_counts()


# In[38]:


get_ipython().run_line_magic('matplotlib', 'inline')
movies.duration.plot(kind='hist')


# In[39]:


movies.content_rating.isnull().sum()


# In[41]:


movies[movies.content_rating.isnull()]


# In[43]:


movies.content_rating.value_counts()


# In[46]:


import numpy as np
movies[movies.content_rating=='NOT RATED'].content_rating=np.nan


# In[47]:


movies.loc[movies.content_rating=='NOT RATED','content_rating']=np.nan


# In[48]:


movies.content_rating.isnull().sum()


# In[53]:


top_movies=movies.loc[movies.star_rating>=9,:].copy()
top_movies


# In[54]:


top_movies.loc[0,'duration']=150


# In[52]:


top_movies


# In[ ]:




