"""
np.insert(array, index, value, axis=none) refers to inserting values along a specified axis in an array.
array is the input array, index is the position where the value will be inserted,
value is the value to be inserted, and axis specifies the axis along which to insert the value
if axis is None, the input array is flattened before insertion.

array - original array to insert values into.
index - position where the value will be inserted.
value - value to be inserted.
axis - specifies the axis along which to insert the value.

axis= 0, insert along rows.(default)
axis= 1, insert along columns.
None - flatten the array before insertion.

"""

import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)

new_arr = np.insert(arr, 2, 100, axis=0)
print(new_arr)
