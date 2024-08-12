#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[19]:


import pandas as pd
df=pd.read_csv(r'C:\Users\SRUTHI\Downloads\phase1\API_SP.POP.TOTL_DS2_en_csv_v2_2001050.csv', skiprows=4)
print(df.head())


# In[20]:


df.shape


# In[21]:


df.columns


# In[22]:


df.dtypes


# In[23]:


df.info()


# In[24]:


df.describe()


# In[25]:


df.duplicated().sum()


# In[26]:


df.isna().sum().any()


# In[27]:


df=df.fillna(method = "ffill")
df.head()


# In[28]:


df.isna().sum().any()


# In[29]:


df['Country Name'].unique()


# In[30]:


df['Country Code'].unique()


# In[31]:


df['Indicator Name'].unique()


# In[32]:


df['Indicator Code'].unique()


# In[33]:


df.drop(['Indicator Name','Indicator Code','Country Code'],axis=1,inplace = True)


# In[34]:


df.columns


# In[35]:


cols = ['1960', '1961', '1962', '1963', '1964', '1965', '1966',
       '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975',
       '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984',
       '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993',
       '1994', '1995', '1996', '1997', '1998', '1999', '2000','2001', '2002', '2003', '2004', '2005', '2006', '2007',
       '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
       '2017', '2018', '2019', '2020', '2021', '2022']


# In[36]:


for i in cols:
        fig=plt.figure(figsize=(5,5))
        plt.hist(df[i],color='#B22222',bins=10)
        plt.xlabel(i)
        plt.show()


# In[37]:


years=df.columns[1:]  
total_values=df[years].sum()
plt.figure(figsize=(30,30))  
plt.barh(years, total_values,color='#191970')
plt.xlabel('Total Values')
plt.ylabel('Year',size=20)
plt.title('Total Values per Year',size=20)
plt.show()


# In[38]:


country_by_1960=df.sort_values(by='1960').head(20)
country_by_1960


# In[39]:


country_by_1960_t=country_by_1960.set_index('Country Name').T
for country_name, data_values in country_by_1960_t.iterrows():
    fig=plt.figure(figsize=(10, 5))
    sns.barplot(x=data_values.index,y=data_values.values)
    plt.xlabel('Countries')
    plt.ylabel('Data Values')
    plt.title(f"{country_name} - Data Values from 1960 to 2022")
    plt.xticks(rotation=90)
    plt.show()


# In[40]:


country_by_2022=df.sort_values(by='2022').head(20)
country_by_2022


# In[41]:


country_by_2022_t=country_by_2022.set_index('Country Name').T
for country_name,data_values in country_by_2022_t.iterrows():
    fig=plt.figure(figsize=(10,5))
    sns.barplot(x=data_values.index,y=data_values.values)
    plt.xlabel('Year')
    plt.ylabel('Data Value')
    plt.title(f"{country_name} - Data Values from 1960 to 2022")
    plt.xticks(rotation=90)
    plt.show()


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[5]:


df=pd.read_csv(r"C:\Users\SRUTHI\Downloads\phase1\Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_2001050.csv")


# In[6]:


df


# In[7]:


gender_counts=df['Region'].value_counts()
bar_width=0.9
x=range(len(gender_counts.index))
plt.bar(gender_counts.index,gender_counts.values)
plt.xlabel('Region')
plt.ylabel('Count')
plt.title('Distribution of Region')
plt.xticks(x,gender_counts.index,rotation=45)
plt.tight_layout()
plt.show()


# In[8]:


df.shape


# In[9]:


df.info


# In[ ]:


df

