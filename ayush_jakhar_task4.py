#!/usr/bin/env python
# coding: utf-8

# In[218]:


import pandas as pd
path="C:\\Users\\ayush\\Downloads\\task_4.csv"
df=pd.read_csv(path)
#print(df.to_string())


# In[219]:


df


# In[220]:


df.isnull().sum()


# In[221]:


df[df['area'].isna()==1]


# In[222]:


df.duplicated().any()


# In[223]:


df.duplicated().sum()


# In[224]:


df.dtypes


# In[225]:


#df['parking'].astype('int')


# In[ ]:





# In[226]:


# df=df.drop(0,axis=0)
# df
# df=df.drop('price',axis=1)
# df



# In[227]:


print(df['stories'].unique())
print(df['bedrooms'].unique())
print(df['bathrooms'].unique())
print(df['mainroad'].unique())
print(df['guestroom'].unique())
print(df['basement'].unique())
print(df['hotwaterheating'].unique())
print(df['airconditioning'].unique())
print(df['parking'].unique())
print(df['prefarea'].unique())
print(df['furnishingstatus'].unique())



# In[228]:


#null_values=["nan","Of course" ,"Indeed", "yep" ,"Haan" ,"True" ,"y", "Y", "['y']"," Nope","Yo","Haanji","Nakko","False" ,"Naaji", "N" ,"n","ille","N","['n']","Nah"]


# In[229]:


#df=pd.read_csv(path,na_values=null_values)


# In[230]:


#df.isnull().sum()


# In[231]:


wtrue=["Of course" ,"Indeed", "yep" ,"Haan" ,"True" ,"y", "Y", "['y']","Yo","Haanji"]
rtrue='yes'
wfalse=["Nope","Nakko","False" ,"Naaji", "N" ,"n","ille","N","['n']","Nah"]
rfalse='no'
df['mainroad']=df['mainroad'].replace(wtrue,rtrue)
df['mainroad']=df['mainroad'].replace(wfalse,rfalse)
df['guestroom']=df['guestroom'].replace(wtrue,rtrue)
df['guestroom']=df['guestroom'].replace(wfalse,rfalse)
df['basement']=df['basement'].replace(wtrue,rtrue)
df['basement']=df['basement'].replace(wfalse,rfalse)
df['hotwaterheating']=df['hotwaterheating'].replace(wtrue,rtrue)
df['hotwaterheating']=df['hotwaterheating'].replace(wfalse,rfalse)
df['airconditioning']=df['airconditioning'].replace(wtrue,rtrue)
df['airconditioning']=df['airconditioning'].replace(wfalse,rfalse)
df['parking']=df['parking'].replace(wtrue,rtrue)
df['parking']=df['parking'].replace(wfalse,rfalse)
df['prefarea']=df['prefarea'].replace(wtrue,rtrue)
df['prefarea']=df['prefarea'].replace(wfalse,rfalse)


# In[ ]:






# In[232]:


#to display specific columns
#display(df.iloc[6])


# In[233]:


df.isnull().sum()


# In[234]:


df=df.fillna({
    'parking':0,
    'bedrooms':1,
    'bathrooms':1,
    'stories':1,
    #'basement':'no'
    #'prefarea':'no'
    
})


# In[235]:


df=df.dropna(subset=['furnishingstatus'])
df=df.dropna(subset=['airconditioning'])
df=df.dropna(subset=['hotwaterheating'])
df=df.dropna(subset=['guestroom'])
#df=df.dropna(subset=['area'])
df=df.dropna(subset=['mainroad'])
df


# In[236]:


df['area']=df['area'].interpolate(method='linear')


# In[237]:


df


# In[242]:


df.to_csv('C:\\Users\\ayush\\OneDrive\\Desktop\\ayush_jakhar_task4\\ayush_jakhar_task4.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




