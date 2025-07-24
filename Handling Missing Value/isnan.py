"""
isnan - Check if a value is NaN (Not a Number)
if the value is NaN, return True; otherwise, return False.

np.isnan(array) is used to check if the value is NaN.
"""

import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])

print(np.isnan(arr))

#print(np.nan == np.nan) #cannot be used to check NaN