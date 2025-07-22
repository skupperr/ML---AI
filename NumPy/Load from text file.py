import numpy as np

filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

print(filedata > 50)

print(filedata[filedata > 50])

# will be true if any data in each column is greater then 50
print( np.any(filedata > 50, axis=0 ))

# will be true if all data in each row is greater then 50
print( np.all(filedata > 50, axis=1 ))

# greater then 50 and less than 100
(((filedata > 50) & (filedata < 100)))

# not greater then 50 and not less then 100
(~((filedata > 50) & (filedata < 100)))