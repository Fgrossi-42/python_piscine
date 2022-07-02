# import pandas as pd
# # from PIL import Image
  
# # img = Image.open("atlanta neighborhood.jpeg")
# # img.show()
# df = pd.read_csv("atlcrime.csv")
# #test = df["crime"].value_counts()
# # print(test)
# df['year'] = pd.DatetimeIndex(df['date']).year
# df['month'] = pd.DatetimeIndex(df['date']).month
# # result1 = result["location"].value_counts()
# result = df[df["crime"] == "LARCENY-FROM VEHICLE"]
# # result = df["location"].value_counts()
# # print(result["location"].value_counts())

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("atlcrime.csv")
order = data.sort_values(by="npu")
npu = order["npu"].dropna().unique()
choice = input("Enter the number of the NPU location you want to see the crimes of:\n\n" + str(npu) + "\n\nenter:")
result1 = data[data["npu"] == choice]#.value_counts()[3:].to_dict()
result = result1["crime"].value_counts()
cars = []
cars2 = []
cars3 = []
max = result.sum()
i = 0
for key, value in result.items():
    cars.append(key)
    cars2.append(value)
    if i == 0:
        cars3.append(0.2)
        i = 4
    else:
        cars3.append(0)
plt.figure(figsize=(14,10))
plt.pie(cars2, labels=None, explode=cars3, startangle=180)
plt.legend(loc="upper left", labels=cars, bbox_to_anchor=(1,1), ncol=1, fancybox=True, shadow=True, prop={'size': 12})
plt.title("THE MOST COMMON CRIME IN THE NPU " + choice, fontsize=20, weight="bold", color="black")
plt.xlabel('the total number of crimes the NPU location ' + choice + ' is ' + str(max), fontsize=12, color='black',
    fontweight='bold', horizontalalignment='center')
plt.show()

# TROUGH THE YEARS CHECK

# result = df[df["month"] == 1]
# print ("\n\njanuary:\n",result["crime"].value_counts())
# result = df[df["month"] == 2]
# print ("\n\nfebruary:\n",result["crime"].value_counts())
# result = df[df["month"] == 3]
# print ("\n\nmarch:\n",result["crime"].value_counts())
# result = df[df["month"] == 4]
# print ("\n\napril:\n",result["crime"].value_counts())
# result = df[df["month"] == 5]
# print ("\n\nmay:\n",result["crime"].value_counts())
# result = df[df["month"] == 6]
# print ("\n\njune:\n",result["crime"].value_counts())
# result = df[df["month"] == 7]
# print ("\n\njuly:\n",result["crime"].value_counts())
# result = df[df["month"] == 8]
# print ("\n\naugust:\n",result["crime"].value_counts())
# result = df[df["month"] == 9]
# print ("\n\nseptember:\n",result["crime"].value_counts())
# result = df[df["month"] == 10]
# print ("\n\noctober:\n",result["crime"].value_counts())
# result = df[df["month"] == 11]
# print ("\n\nnovember:\n",result["crime"].value_counts())
# result = df[df["month"] == 12]
# print ("\n\ndecember:\n",result["crime"].value_counts())
 
 