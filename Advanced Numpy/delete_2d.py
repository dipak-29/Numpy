import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Original 2D array:\n", arr_2d)

new_arr_2d = np.delete(arr_2d, 0, axis=0)  # Remove the  first row
print("Array after deletion:\n", new_arr_2d)

