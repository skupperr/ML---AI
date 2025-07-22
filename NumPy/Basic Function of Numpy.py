import numpy as np

a = np.array([1,2,3], dtype= 'int16')
print(a)

b = np.array([[1.0,2.3,3.0], [5.0,6.0,7.0]])
print(b)

# Get dimension
print("Dim:")
print(a.ndim)
print(b.ndim)

# Get shape
print("Shape: ")
print(a.shape)  
print(b.shape)  # 2 by 3 (2 rows and 3 columns)

print("DType: ")
print(a.dtype)
print(b.dtype)

# Get size
print("Item Size:")
print(a.itemsize)
print(b.itemsize)

# number of elements
print("Number of elements: ")
print(a.size)
print(b.size)

# Number of bytes
print("Number of bytes: ")
print(a.nbytes)
print(b.nbytes)

#copy
x = np.array([1,2,3])
y = x.copy()
print(y)