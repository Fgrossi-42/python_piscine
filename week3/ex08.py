import pandas as pd

df=pd.read_csv('Salaries.csv')
item_counts = df["JobTitle"].nunique()
print(item_counts)