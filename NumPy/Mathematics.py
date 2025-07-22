import numpy as np

# https://numpy.org/doc/stable/reference/routines.math.html

a = np.array([1,2,3,4])
print(a+2)

a += 4
print(a)

b = np.array([1,0,1,0])
print(a+b)



arr = np.array([0, 30, 60, 90])
x = np.deg2rad(arr)

print(x)

print(np.sin(x))
print(np.cos(x))
print(np.tan(x))


# Round
numbers = np.array([1.23456, 2.34567, 3.45678, 4.56789])

# round the array to two decimal places
rounded_array = np.round(numbers, 2)

print(rounded_array)

# floor & ceiling
print("Array after floor():", np.floor(numbers))
print("Array after ceil():", np.ceil(numbers))



'''         Linear Algebra          '''
# https://numpy.org/doc/stable/reference/routines.linalg.html


a = np.ones((2,3))
b = np.full((3,2), 2)
print(a)
print(b)

# matrix multiplication
print(np.matmul(a,b))

# determinant of matrix
a = np.array([[1, 2], [3, 4]])
print(np.linalg.det(a))



'''         Statistics              '''
# https://numpy.org/doc/stable/reference/routines.statistics.html

stats = np.array([[1,2,3],[4,5,6]])
print(np.min(stats))
print(np.max(stats, axis=1))
print(np.sum(stats, axis=0))

# percentile
a = np.array([[10, 7, 4], [3, 2, 1]])
print("Percentile:", np.percentile(a, 50) )

# Quantile
print("Quantile:", np.quantile(a, 0.5) )

# mean
print("Mean:", np.mean(a) )

# meadian
print("Median:", np.median(a) )