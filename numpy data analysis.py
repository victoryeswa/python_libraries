#pip install numpy incase you have not install
import numpy as np

#The basics
a = np.array([1,2,3])
print(a)
#2d-array
b = np.array([[9.0,8.0,7.0,],[6.0,5.0,4.0]])
print(b)
#get dimension
print(a.ndim)
#get shape
print(b.shape,'shape')
#get type
print(a.dtype)
#get size
print(a.itemsize) 
#get total size
print(a.nbytes)
#Note - floats are bigger than integers
#ACCESSING/CHANGING specific elements, rows, columns etc
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
#get a specific element in[r,c]
print(a[1,2])
#get a specific row
print(a[0, :])
#get a specific column
print(a[:, 2])
#getting fancier [startindex:endindex:stepsize]
print(a[0,1:-1:2])
#assigning values
a[1,5] = 20
print(a)

a[:,2] = [1,2]
print(a)
# *3D example
b = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(b)
#get specific elements(work outside in)
print(b[:,1,:])
#replace
b[:,1,:]= [2]
print(b)
#initializing different types of array
#All 0s matrix
print(np.zeros((2,3,3,2)))
#all 1s mtrix
print(np.ones((4,2,2),dtype='int32'))
#Any other number
print(np.full((2,2),99, dtype='float32'))
#any other number (full_like)
print(np.full(a.shape, 4))
#random decimal numbers
print(np.random.rand(4,2))
#random_sample method
print(np.random.random_sample(a.shape))
#random integer values
print(np.random.randint(-2,7,size=(3,3)))
#the identity matrix
print(np.identity(5))
#repeat an array
arr = np.array([1,2,3])
r1 = np.repeat(arr,3, axis=0)
print(r1)

output = np.ones((5,5))
print(output)
z= np.zeros((3,3))
z[1,1] = 9
print(z)
output[1:-1,1:-1]=z
print(output)
#be careful when copying arrays
a = np.array([1,2,3])

b = a.copy()
b[0] = 100
print(b)
print(a)
#Mathematics
a = np.array([1,2,3,4])
print(a)
print(a+2, 'sum+2')
print(a/2, 'div.by 2')
print(a*2, 'mult.by 2')

b = np.array([1,0,1,0])
print(a+b)
#take the sin
print(np.sin(a))
#Linear Algebra
a = np.full((2,3),1)
print(a)
b = np.full((3,2), 2)
print(b)
# multiplying using np
print(np.matmul(a,b))
#find the determinant
c = np.identity(3)
print(np.linalg.det(c))
#Statistics
stats = np.array([[1,2,3],[4,5,6]])
print(stats)
print(np.min(stats))
print(np.max(stats, axis=1))
print(np.sum(stats, axis=0))
#Reorganizing Arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
after = before.reshape((2,2,2))
print(after)
#vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2,v1,v2]))
#Horizontal stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))

print(np.hstack([h1,h2,h1,h2]))
#Boolean Masking and Advanced Indexing



