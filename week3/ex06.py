import pandas as pd

df=pd.read_csv('Salaries.csv')
result = df[df["TotalPayBenefits"] == df['TotalPayBenefits'].min()]

print(result["EmployeeName"])
print("il poraccio sta in negativo oh")