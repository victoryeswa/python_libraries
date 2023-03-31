import numpy as np
#The basics

a = np.array([1, 2,3])

print(a)

b = np.array([[9, 8, 7], [6, 5, 4]])

print(b)

#Get dimension
a.ndim

#get shape
b.shape

#get type
a.dtype

#get size
a.itemsize

#get total size
a.size * a.itemsize

#get total size
a.nbytes

#Accessing/changing specific elements, rows, columns

a = np.array([[1, 2,3, 4, 5, 6, 7, 8, ], [8, 10, 11, 12, 13, 14]])
print(a)

#get a specific element[r, c]

a[1, 5]

#get a specific row
a[0, :]

#get a specific column
a[:, 2]

#Getting a little more fancy [startindex:endindex:stepsize]
a[0, 1: 6:2]

a[1, 5] = 20

print(a)

a[:, 2] = [1,2]
print(a)


#3d example
b = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])
print(b)

#get a specific element (ork outside in)

print(b[:, 1, 1])


















