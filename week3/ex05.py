import pandas as pd

df=pd.read_csv('Salaries.csv')
result = df.loc[df["TotalPayBenefits"] == df['TotalPayBenefits'].max(), "EmployeeName"].values[0]
print(result)