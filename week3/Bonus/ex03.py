import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("titles.csv")


data = data[data["production_countries"] == "['US']"]
result2 = {}
for x, y in data["tmdb_popularity"].sort_values(ascending=False)[:1].to_dict().items():
        result2[x] = (y, data["production_countries"].to_dict()[x], data["release_year"].to_dict()[x])

# print(result2)

result3 = data[["production_countries", "release_year" , "tmdb_popularity"]].sort_values(by="tmdb_popularity",ascending=False)[:1]
cars = []
cars2 = []

i =0
cars.append(result3['release_year'].values[0])
cars2.append(result3['tmdb_popularity'].values[0])

plt.pie(cars2, labels=cars, autopct='%1.2f%%')
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
plt.show()