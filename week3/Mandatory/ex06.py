import pandas as pd

df=pd.read_csv('Salaries.csv')
result = df.loc[df["TotalPayBenefits"] == df['TotalPayBenefits'].min(), "EmployeeName"].values[0]

print(result)
print("il poraccio sta in negativo oh")