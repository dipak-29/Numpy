"""
splitting refers to the process of dividing an array into multiple sub-arrays.

np.split() splits an array equally into multiple sub-arrays along a specified axis.

np.hsplit() is a specific case of np.split() that splits an array horizontally (along axis 1).

np.vsplit() is a specific case of np.split() that splits an array vertically (along axis 0).
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(np.split(arr, 2))  # Split the array into 2 equal parts

print(np.hsplit(arr, 3))  # Split the array into 3 equal parts horizontally

