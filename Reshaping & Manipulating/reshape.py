"""
#reshaping refers to changing the shape of an array without changing its data.

reshape(rows,columns) specify new shape of the array.
if only dimensions match, it will reshape the array.

reshaping does not create a copy of the data, it only changes the view of the data.


"""


import numpy as np

arr = np.array([10, 20, 30, 40, 50,60])
reshaped_arr = arr.reshape(2, 3)  # Reshape to 2 rows and 3 columns
print(reshaped_arr)