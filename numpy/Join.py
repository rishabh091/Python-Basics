import numpy as np


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])
om
print(np.stack((arr1, arr2, arr3)))

# stacking along rows
print(np.hstack((arr1, arr2, arr3)))

# stacking along columns
print(np.vstack((arr1, arr2, arr3)))

# stacking along depth
print(np.dstack((arr1, arr2, arr3)))

