import numpy as np

arr1 = np.array([[1,2,3], [4,5,6]])  # 2D array
arr2 = np.array([1,2]) #shape(2,)  # 1D array

result = arr1 + arr2  # Broadcasting the 1D array across the rows of the 2D array
print(result)

#.reshape() can be used to change the shape of an array if needed, but in this case, it is not necessary as broadcasting handles the operation directly.

