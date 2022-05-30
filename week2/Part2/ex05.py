import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mimg

def mat(n):
	array = np.arange(n -1)/(n - 1)
	array = np.append(array, 1)
	return array

def imag(m, n):
	matrix = []
	for x in range(m):
		matrix = np.append(matrix, mat(n))
	matrix = matrix.reshape(m, n)
	return matrix

img = mimg.imread("/goinfre/fgrossi/python_piscine/week2/Part2/ex01.png")
print(img.shape)
img2 = img.reshape(img.shape[0] * img.shape[1], img.shape[2])
matrix = imag(img.shape[2], img.shape[2])
c = np.matmul(img2, matrix)
output = c.reshape(img.shape[0], img.shape[1], img.shape[2])

plt.imshow(output)
plt.show()