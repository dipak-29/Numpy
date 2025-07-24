#filtering or boolean masking is a way to access elements of an array based on a condition

import numpy as np

arr = np.array([10, 20, 30, 40, 50,60])

print(arr[arr > 30])  # Accessing elements greater than 30