import numpy as np

def func(n) :
    arrayF = np.arange(0, 1 + (1/n), 1/(n - 1))
    return arrayF

print(func(int(input("dimensioni array: "))))