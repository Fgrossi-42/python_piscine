import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import array as arr

df = pd.read_csv("atlcrime.csv")
df['year'] = pd.DatetimeIndex(df['date']).year
df['month'] = pd.DatetimeIndex(df['date']).month
result = df[df["year"] == 2009]
print ("\n\n2009:\n",result["crime"].value_counts().sum())
result = df[df["year"] == 2010]
print ("\n\n2010:\n",result["crime"].value_counts().sum())
result = df[df["year"] == 2011]
print ("\n\n2011:\n",result["crime"].value_counts().sum())
result = df[df["year"] == 2012]
print ("\n\na2012:\n",result["crime"].value_counts().sum())
result = df[df["year"] == 2013]
print ("\n\n2013:\n",result["crime"].value_counts().sum())
result = df[df["year"] == 2014]
print ("\n\n2014:\n",result["crime"].value_counts().sum())
result = df[df["year"] == 2015]
print ("\n\n2015:\n",result["crime"].value_counts().sum())
result = df[df["year"] == 2016]
print ("\n\n2016:\n",result["crime"].value_counts().sum())
