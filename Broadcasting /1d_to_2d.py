import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]]) #2*3 matrix

vector = np.array([10, 20, 30])  # 1D array

result = matrix + vector  # Broadcasting the vector across the rows of the matrix
print(result)