import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("titles.csv") 
result = data["type"].value_counts()[:10].to_dict()
print(result)
cars = []
cars2 = []
cars3 = []
max = data["type"].value_counts()[:10].sum()
i =0
for key, value in result.items():
    cars.append(key)
    cars2.append(value)
    if i == 0:
        cars3.append(0.2)
        i = 4
    else:
         cars3.append(0.05)
plt.pie(cars2, labels=cars, explode=cars3, autopct='%1.2f%%',
     shadow=True)
plt.title("NETFLIX &&&&&&&&&& CHILL")
plt.xlabel('The number of films and shows is: ' + str(max))
plt.show()