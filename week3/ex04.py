import pandas as pd

df = pd.read_csv("Salaries.csv")
result = df.loc[df["EmployeeName"] == "JOSEPH DRISCOLL", "TotalPayBenefits"].values[0]

print (result)