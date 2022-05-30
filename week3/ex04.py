import pandas as pd

df = pd.read_csv("Salaries.csv")
result = df[df["EmployeeName"] == "JOSEPH DRISCOLL"]

print (result["TotalPayBenefits"])