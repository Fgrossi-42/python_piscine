import numpy as np
import matplotlib.pyplot as plt

def func(n) :
    arrayF = np.arange(0, 1 + (1/n), 1/(n - 1))
    return arrayF

n = func(int(input("colonne array: ")))
m = int(input("righe array: "))
result = np.tile(n,(m,1))
plt.imshow(np.asarray(result))
plt.colorbar()
plt.show()