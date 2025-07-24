"""
vertically stacking refers to stacking arrays on top of each other,
while horizontally stacking refers to stacking arrays side by side.

vstack() is used for vertical stacking,

hstack() is used for horizontal stacking.
"""


import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print(np.vstack((arr1, arr2)))  # Vertical stacking
print(np.hstack((arr1, arr2)))  # Horizontal stacking