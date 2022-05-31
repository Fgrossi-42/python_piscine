import pandas as pd

df=pd.read_csv('Salaries.csv')
p=df['BasePay'].mean()

print(p)