import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# will traverse multi dimensional array element by element
"""Here arr means arr to traverse using nditer
flags=['buffered'] means to store converted data in buffer
op_dtypes=str means treat data as string"""
for x in np.nditer(arr, flags=['buffered'], op_dtypes=str):
    print(x)

# Enumerate data, i.e get index and value using ndenumerate
for i, value in np.ndenumerate(arr):
    print('Index : {} and Value : {}'.format(i, value))

