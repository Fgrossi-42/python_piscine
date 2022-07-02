import pandas as pd
# from PIL import Image
  
# img = Image.open("atlanta neighborhood.jpeg")
# img.show()
df = pd.read_csv("atlcrime.csv")
#test = df["crime"].value_counts()
# print(test)
df['year'] = pd.DatetimeIndex(df['date']).year
df['month'] = pd.DatetimeIndex(df['date']).month
# result1 = result["location"].value_counts()
result = df["npu"].value_counts()
print(result)