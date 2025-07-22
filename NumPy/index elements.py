import numpy as np

a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])

# Get a specific elements
print(a[1,5])

# Get a specific row
print(a[1, :])

# Get a specific column
print(a[:, 5])

# printing 2,4,6 [row, startindex : endindex : stepsize]
print(a[0, 1:6:2])

# changing elements
a[1,5] = 20
print(a)

# changing whole row
a[0, :] = 5
print(a)