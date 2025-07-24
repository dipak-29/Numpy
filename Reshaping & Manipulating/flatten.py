#flattening refers to converting a multi-dimensional array into a one-dimensional array.

"""
#ravel() returns a flattened array, which is a view of the original array.
#flatten() returns a copy of the original array, flattened into one dimension.

"""

import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)

print(arr_2d.ravel())

print(arr_2d.flatten())


