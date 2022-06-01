import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("titles.csv") 
result = data["release_year"].value_counts()[:10].to_dict()
cars = []
cars2 = []
cars3 = []
max = data["release_year"].value_counts()[:10].sum()
i =0
for key, value in result.items():
    cars.append(key)
    cars2.append(value)
    if i == 0:
        cars3.append(0.2)
        i = 4
    else:
         cars3.append(0.05)
plt.figure(figsize=(10,10))
plt.pie(cars2, labels=cars, explode=cars3, autopct='%1.2f%%',
     shadow=False)
plt.title("NETFLIX &&&&&&&&&& CHILL")
plt.xlabel('The number of films in the year between 2013-2021 is: ' + str(max))
plt.show()