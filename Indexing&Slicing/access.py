#indexing refers to accessing elements of a sequence
#indexing is done using square brackets
#indexing for 2d arrays is done using a comma to separate row and column indices


"""
array[index] #1d array access
array[row, column] #2d array access
"""

import numpy as np

arr = np.array([10,20,30,40,50])

print(arr[0])  # Accessing the first element
print(arr[2])  # Accessing the third element
print(arr[-1]) # Accessing the last element