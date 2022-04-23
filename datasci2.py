#!/usr/bin/env python
# coding: utf-8

# In[2]:


# ESSENTIAL LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


# In[3]:



# USE PANDAS BUILTIN FUNCTION TO READ FILE
df = pd.read_csv("data2.csv")


# In[4]:



# DATAFRAME OF COUNTRIES
cn_df = df["Country Name"]


# In[5]:



# REMOVE REPITITION IN COUNTRIES DATA FRAME
countries = [ ]
for i in cn_df:
    if i not in countries:
        countries.append(i)


# In[6]:


# MAKE METHOD THAT USE FOR CONVERTING INTO LIST

def toList(args):
    lst = list()
    for i in args:
        lst.append(int(i))
    return lst

# CALLING METHOD 
years_df = df.iloc[0:0,5:-1]
years = toList(years_df)


# In[7]:


# CO2 EMISSION IN CHINA
def CO2INCHINA():
#     SPECIFIC ROW VIA PANDAS
    df_china = df.loc[(df['Country Name'] == "China") & (df['Indicator Name'] == "CO2 emissions from solid fuel consumption (% of total)")]
    
#     MAKE ARRAY
    df_china_data = df_china.iloc[:,5:-1].values
    
#     REMOVE NULL
    df_china_data=df_china_data[np.logical_not(np.isnan(df_china_data))] 
    
#     MAKE LIST
    datalist = list(df_china_data)
    
#     PLOT VIA SEABORN
    sb.distplot(datalist, kde=True, color = "r")
CO2INCHINA()


# In[8]:


def co2EmissionDenmark():
    
#     SPECIFIC ROW VIA PANDAS
    df_denmark = df.loc[(df['Country Name'] == "Denmark") & (df['Indicator Name'] == "CO2 emissions from solid fuel consumption (% of total)")]
    
#     ARRAY MAKING
    df_denmark_data = df_denmark.iloc[:,5:-1].values
    
#     REMOVE NULL
    df_denmark_data=df_denmark_data[np.logical_not(np.isnan(df_denmark_data))] 
   
#     CONVERT TO LIST
    datalist = list(df_denmark_data)
    
#     SEABORN TO PLOT
    sb.distplot(datalist, kde=True, color = "b")
co2EmissionDenmark()


# In[51]:


def co2EmissionGermany():
    
#     ONLY SPECIFIC INDICATOR
    df_Germany = df.loc[(df['Country Name'] == "Germany") & (df['Indicator Name'] == "CO2 emissions from solid fuel consumption (% of total)")]
    
#     MAKING ARRAY OF THAT 
    df_Germany_data = df_Germany.iloc[:,5:-1].values
    
#     REMOVE NULL 
    df_Germany_data=df_Germany_data[np.logical_not(np.isnan(df_Germany_data))] 
    
#     CONVERT TO LIST 
    datalist = list(df_Germany_data)
    
#     PLOTING
    sb.distplot(datalist, kde=True, color = "g")

    
# CALLING
co2EmissionGermany()


# In[58]:


def comparison():
    
# INDICATOR 1
    df_Germany_co2 = df.loc[(df['Country Name'] == "Germany") & (df['Indicator Name'] == "CO2 emissions from solid fuel consumption (% of total)")]
    df_Germany_data1 = df_Germany_co2.iloc[:,5:-1].values
    df_Germany_data1=df_Germany_data1[np.logical_not(np.isnan(df_Germany_data1))] 
    
    dataOfCo2 = list(df_Germany_data1)
    
    
# INDICATOR 2
    df_Germany_elect = df.loc[(df['Country Name'] == "Germany") & (df['Indicator Name'] == "Electricity production from coal sources (% of total)")]
    df_Germany_data2 = df_Germany_elect.iloc[:,5:-1].values
    df_Germany_data2=df_Germany_data2[np.logical_not(np.isnan(df_Germany_data2))] 
    
    dataOfelec = list(df_Germany_data2)
    plt.figure(figsize=(20,15))

#     PLOTING 1
    sb.distplot(dataOfCo2, kde=True, color = "g")
    
#     PLOTING 2
    sb.distplot(dataOfelec, kde=True, color = "r")

    
# CALLING     
comparison()
    


# In[ ]:




