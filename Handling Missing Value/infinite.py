#np.isinf() - Check if a value is infinite
#1/0
# if the value is infinite, return True; otherwise, return False.

import numpy as np

arr = np.array([1, 2, np.inf, 4, -np.inf, 6])

print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr, posinf=1000, neginf=-100)
print(cleaned_arr)