"""
np.delete() refers to the process of removing elements from an existing array in NumPy.
it removes elements along a specified axis.

np.delete(array, index, axis=None) removes the element at the specified index along the given axis.

"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50,60])
print("Original array:", arr)

new_arr = np.delete(arr, 0 )  # Remove the element at index 2
print("Array after deletion:", new_arr)