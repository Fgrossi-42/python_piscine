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



from turtle import color
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import math
import array as arr

data = pd.read_csv("atlcrime.csv")
plot1 = plt.subplot2grid((3, 3), (0, 0), colspan=2, fig= plt.figure(figsize=(20,10)))
plot2 = plt.subplot2grid((3, 3), (0, 2), rowspan=3, colspan=2)
plot3 = plt.subplot2grid((3, 3), (1, 0), rowspan=6, colspan=2)
cars = []
cars2 = []
cars3 = []
i = 0

order = data.sort_values(by="npu")
npu = order["npu"].dropna().unique()
choice = input("Enter the number of the NPU location you want to see the crimes of:\n\n" + str(npu) + "\n\nenter: ")
if choice.upper() not in npu:
    print("Invalid input")
    exit()
result1 = data[data["npu"] == choice.upper()]
result = result1["crime"].value_counts()
max = result.sum()
for key, value in result.items():
    cars.append(key)
    cars2.append(value)
    if i == 0:
        cars3.append(0.2)
        i = 4
    else:
        cars3.append(0)
plot3.pie(cars2, labels=None, explode=cars3, startangle=180)
plot3.legend(loc="upper left", labels=cars, bbox_to_anchor=(1,1), ncol=1, fancybox=True, shadow=True, prop={'size': 12})
plot3.set_title("THE MOST COMMON CRIME IN THE NPU " + choice.upper(), fontsize=20, weight="bold", color="black", style="italic")
plt.xlabel('the total number of crimes the NPU location ' + choice.upper() + ' had is ' + str(max), fontsize=12, color='black',
    fontweight='bold', horizontalalignment='center')

beat = data["beat"].value_counts()
a = arr.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
for key, value in beat.items():
	if str(key)[0] == '1':
		a[1] += int(value)
	elif str(key)[0] == '2':
		a[2] += int(value)
	elif str(key)[0] == '3':
		a[3] += int(value)
	elif str(key)[0] == '4':
		a[4] += int(value)
	elif str(key)[0] == '5':
		a[5] += int(value)
	elif str(key)[0] == '6':
		a[6] += int(value)
	else:
		a[7] += int(value)
zones = {'Zone 1':a[1], 'Zone 2':a[2], 'Zone 3':a[3], 'Zone 4':a[4], 'Zone 5':a[5], 'Zone 6':a[6], 'Other Zones':a[7]}
courses = list(zones.keys())
values = list(zones.values())
plot2.bar(courses, values, color ='maroon', width = 0.4)
# plt.ylabel("No. of crimes beaten for zones")
plot2.set_title("Division of crimes beaten for Zone", fontsize=18, weight="bold", color="black", style="italic")
plot2.set_ylabel("No. of crimes beaten for zones", fontsize=12, color='black', weight="bold")
plt.tight_layout()
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
 
 