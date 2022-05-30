import pandas as pd

df=pd.read_csv('Salaries.csv')
p=df['BasePay'].median()

print(p)