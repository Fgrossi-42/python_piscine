import numpy as np

matrix = np.random.randint(10, size=(10, 12))
mini_matrix = matrix[0:4, 8:]
print(matrix)
print(mini_matrix)