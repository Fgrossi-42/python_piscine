import pandas as pd

df = pd.read_csv("atlcrime.csv")
test = df["crime"].value_counts()
# print(test)
result = df[df["location"] == "HOMICIDE"]
result1 = result["location"].value_counts()
print (result1)