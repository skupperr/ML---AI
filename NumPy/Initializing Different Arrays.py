import numpy as np

# all zeros
a = np.zeros([2,3])
print(a)

# all 1s
a = np.ones([2,3])
print(a)

# any other numbers
a = np.full((2,2), 99, )
print(a)

# array of randon number
a = np.random.rand(1,3)
print(a)

# random int
a = np.random.randint(5,10, size= (2,2))
print(a)

# identity matrix
print(np.identity(3))

# Repeat an array
a = np.array([[1,2,3]])
r1 = np.repeat(a, 3, axis=0)
print(r1)


'''
        1   1   1   1   1
        1   0   0   0   1
        1   0   9   0   1
        1   0   0   0   1
        1   1   1   1   1

'''

a = np.ones([5,5], dtype='int16')
middle = np.zeros([3,3])
middle[1,1] = 9

a[1:4, 1:4] = middle
print(a)