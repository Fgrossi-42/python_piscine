import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("titles.csv")


data = data[data["production_countries"] == "['US']"]
popul2 = data.groupby("release_year").mean()["tmdb_popularity"].sort_values(ascending=False)[:10].to_dict()

cars = []
cars2 = []

i =0
for key, value in popul2.items():
    cars.append(key)
    cars2.append(value)
print(popul2)
plt.figure(figsize=(10,10))
plt.pie(cars2, labels=cars, autopct='%1.2f%%')
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
plt.show()