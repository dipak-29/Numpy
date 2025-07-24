"""
append refers to the process of adding elements to an existing array in NumPy.
it adds elements to the end of an array along a specified axis.

"""

import numpy as np

arr = np.array([10, 20, 30])

new_arr = np.append(arr, [40, 50, 60])

print(new_arr)