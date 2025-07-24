"""
np.concatenate refers to the process of joining two or more arrays along an existing axis.
it combines arrays into a single array.

np.concatenate((array1, array2), axis=0) combines array1 and array2 along the first axis (rows).

axis 0 > vertical stacking
axis 1 > horizontal stacking

vertical stacking refers to stacking arrays on top of each other,
while horizontal stacking refers to stacking arrays side by side.
"""

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

new_arr = np.concatenate((arr1, arr2), axis=0)
print(new_arr)