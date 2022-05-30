import pandas as pd

df=pd.read_csv('Salaries.csv')
item_counts = df["JobTitle"].value_counts()
print(item_counts[:5])