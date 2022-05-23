import numpy as np

arrayZ = np.zeros(10)
arrayO = np.ones(10)
arrayR = np.arange(start=10, stop=51, step=2)
arrayM = np.identity(3)
rng = np.random.default_rng()
rando = rng.integers(2, size=1)
arrayF = np.arange(start=0, stop=1, step=0.111111111)

print(arrayZ)
print(arrayO)
print(arrayR)
print(arrayM)
print(rando)
print(arrayF)