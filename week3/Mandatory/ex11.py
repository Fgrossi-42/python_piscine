import pandas as pd

df = pd.read_csv("Salaries.csv")
result = df["JobTitle"]
k = 0;
for i in result:
    if "chief" in i.lower():
        k += 1
print (k)