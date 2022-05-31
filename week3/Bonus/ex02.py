import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("titles.csv") 
result = data["genres"].value_counts()[:10].to_dict()
cars = []
cars2 = []
cars3 = []
max = data["genres"].value_counts()[:10].sum()
i =0
for key, value in result.items():
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
#plt.title("NETFLIX &&&&&&&&&& CHILL")
#plt.xlabel('The number of films and shows is: ' + str(max))

result2 = {x: (y, data["genres"].to_dict()[x]) for x, y in data["imdb_score"].sort_values(ascending=False)[:10].to_dict().items()}

print(result2)
cars = []
cars2 = []
cars3 = []
# max = data["genres"].
i =0
for key, value in result2.items():
    cars.append(value[1])
    cars2.append(value[0])
    print(value[1])
    if i == 0:
        cars3.append(0.2)
        i = 4
    else:
        cars3.append(0.05)
pathces, texts, autotexts = ax2.pie(cars2, labels=cars, explode=cars3, autopct='%1.2f%%')
#plt.title("NETFLIX &&&&&&&&&& CHILL")
#plt.xlabel('The number of films and shows is: ' + str(max))
plt.setp(autotexts, size='x-small')

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
plt.show()