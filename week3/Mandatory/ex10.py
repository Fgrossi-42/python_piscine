import pandas as pd

df=pd.read_csv('Salaries.csv')
result = df[df["Year"] == 2013]
pollo = result["JobTitle"].value_counts()
k = 0
for i in pollo:
    if i == True:
        k += 1
print(k)