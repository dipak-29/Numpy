#astype defines to convert data type of a numpy array.

import numpy as np

arr = np.array([1.2, 2.5, 3.8, 4.1])
print(arr)
print(arr.dtype)

int_arr = arr.astype(int)
print(int_arr)

print(int_arr.dtype)

