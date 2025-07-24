#slicing refers to accessing a range of elements in a sequence

"""
#slicing is done using a colon inside square brackets

array[start:stop:step]

array[start:stop] #default step is 1

negative step, -1 reverse

"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50,60])

print(arr[1:5]) #indexes 1 to 4 (5 is not included)

print(arr[:4]) # indexes 0 to 3 (4 is not included)

print(arr[::2]) # every second element # from the start to the end

print(arr[::-1]) # reversing the array