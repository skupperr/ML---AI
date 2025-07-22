import numpy as np

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((4,2))
print(after)

# Vertical stack
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print( np.vstack([v1,v2,v1,v2]) )

# Horizontal stack
print( np.hstack([v1,v2]) )
print( np.hstack([v2,v1]) )