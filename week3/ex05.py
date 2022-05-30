import pandas as pd

df=pd.read_csv('Salaries.csv')
result = df[df["TotalPayBenefits"] == df['TotalPayBenefits'].max()]

print(result["EmployeeName"])