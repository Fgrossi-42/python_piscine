import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import ast

df = pd.read_csv("titles.csv") 
df["genres"] = df["genres"].map(ast.literal_eval)
result = df.explode("genres")
popul = result.groupby("genres").mean()["tmdb_popularity"].sort_values(ascending=False)[:10].to_dict()
print(popul)
cars = []
cars2 = []
cars3 = []
i =0
for key, value in popul.items():
    cars.append(key)
    cars2.append(value)
    if i == 0:
        cars3.append(0.2)
        i = 4
    else:
        cars3.append(0.05)
fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)
fig.suptitle("NETFLIX &&&&&&&&&& CHILL")
pathces, texts, autotexts = ax1.pie(cars2, labels=cars, explode=cars3, autopct='%1.2f%%')
plt.setp(autotexts, size='x-small')

popul2 = result.groupby("genres").mean()["imdb_score"].sort_values(ascending=False)[:10].to_dict()

print(popul2)
cars = []
cars2 = []
cars3 = []
i =0
for key, value in popul2.items():
    cars.append(key)
    cars2.append(value)
    if i == 0:
        cars3.append(0.2)
        i = 4
    else:
        cars3.append(0.05)
pathces, texts, autotexts = ax2.pie(cars2, labels=cars, explode=cars3, autopct='%1.2f%%')
plt.setp(autotexts, size='x-small')

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
plt.show()