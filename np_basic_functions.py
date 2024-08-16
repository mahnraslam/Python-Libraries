a = [[2,3,4],[3,4,5],[3,5,4],[3,4,6],[5,4,3]]
for i in range(1,len(a),2):
    for j in range(0,3,2):
        print(a[i][j],end=" ")
    print()

import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,5])
print(a.itemsize)         #BYtes
print(a.ndim)
print(a.shape)
print(a.size)
print(a+b)
print(np.dot(a,b))
#print(np.linespace(-2,5,num=4))
#z = np.linespace(0,2,10)
z = [[2,3,4],[2,3,4]]
x = [[2,3],[7,1],[2,4]]
z = np.array(z)
print(z.size)
print(z.ndim)
print(z.shape)
print(np.dot(x,z))
arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])
arrayOne = arrayOne + arrayTwo
print(arrayOne**2)

a = [[10, 11, 12],
 [13, 14, 15],
 [16, 17, 18],
 [19, 20, 21],
 [22, 23, 24],
 [25, 26, 27],
 [28, 29, 30],
 [31, 32, 33]]

#subArrays = np.split(a, 4)
#print(subArrays)
arr1 = np.array([[7,4,0],[88,5,7]])
arr2 = np.random.randint(low = 1, high = 100, size = 6).reshape(2,3)
print("arr1 = ", arr1)
print("arr2 = ", arr2)

arr3 = np.concatenate((arr1, arr2))
arr3 = np.concatenate((arr1, arr2), axis=0)

arr3 = np.dstack((arr1, arr2))

print ("\nnp.vstack((arr1, arr2)):\n ", arr3)

# The np.vsplit() method is used to split an array into multiple sub-arrays vertically (row-wise). Not applicable for 1-D array.

