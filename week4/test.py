import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import array as arr

# variables

plot1 = plt.subplot2grid((3, 3), (0, 0), colspan=2, fig= plt.figure(figsize=(20,10)))
plot2 = plt.subplot2grid((3, 3), (0, 2), rowspan=3, colspan=2)
plot3 = plt.subplot2grid((3, 3), (1, 0), rowspan=6, colspan=2)
cars = []
cars2 = []
cars3 = []
i = 0
crimes = []
years = range(2009, 2017)
data = pd.read_csv("atlcrime.csv")
data['year'] = pd.DatetimeIndex(data['date']).year

# code for the plot1 line chart

sort = data.sort_values(by="npu")
order = data.sort_values(by="npu")
npu = order["npu"].dropna().unique()
choice = input("Enter the number of the NPU location you want to see the crimes of:\n\n" + str(npu) + "\n\nenter: ")
if choice.upper() not in npu:
    print("Invalid input")
    exit()
for a in years:
	result = data[data["year"] == a]
	result1 = result[result["npu"] == choice.upper()].value_counts().sum()
	crimes.append(result1)
print(crimes)


# code for the plot2 bar graph

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
banana = data[data["npu"] == choice.upper()]
zone = banana["beat"].median()

# code for the plot3 pie chart

result1 = data[data["npu"] == choice.upper()]
result = result1["crime"].value_counts()
max = result.sum()
for key, value in result.items():
    cars.append(key)
    cars2.append(value)
    if i == 0:
        cars3.append(0.1)
        i = 4
    else:
        cars3.append(0)

plot1.plot(years, crimes, color='red', linewidth=2, linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12, label='crime', antialiased=True)
plot1.set_ylim(ymin=0, ymax=5000, auto=True)
plot1.set_ylabel('the number of crimes', fontsize=12, color='black', weight="bold")
plot1.set_title('the total number of crimes during the years', fontsize=20, weight="bold", color="black", style="italic")

colors = ["r" if int(str(zone)[0]) != i else "b" for i in range(1,8)]
plot2.bar(courses, values, color=colors, width = 0.4)
plot2.set_title("Division of crimes beaten for Zone", fontsize=18, weight="bold", color="black", style="italic")
plot2.set_ylabel("No. of crimes beaten for zones", fontsize=12, color='black', weight="bold")
plot2.set_xlabel("the NPU you selected is in zone " + str(zone)[0], fontsize=12, color='black', weight="bold")


plot3.pie(cars2, labels=None, explode=cars3, startangle=180)
plot3.legend(loc="upper left", labels=cars, bbox_to_anchor=(1,1), ncol=1, fancybox=True, shadow=True, prop={'size': 12})
plot3.set_title("THE MOST COMMON CRIME IN THE NPU " + choice.upper(), fontsize=20, weight="bold", color="black", style="italic")
plot3.set_xlabel('the total number of crimes the NPU location ' + choice.upper() + ' had is ' + str(max), fontsize=12, color='black',
    fontweight='bold', horizontalalignment='center')

plt.tight_layout()
plt.show()