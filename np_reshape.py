import numpy as  np
array = np.arange((15)).reshape(3,5)
print(array)

#Array slicing
sub_array = array[1:2,1:4]
print(sub_array)

#Reversing
arr = sub_array[:,::-1]
# The only difference is that arr1[::] explicitly specifies the step size, while arr1[:] does not (it implicitly uses a step size of 1).
arr1 = [12,32,1,2,1,21,2,34,65,4]
print(arr1[:])
print(arr[::])

#Second way
rows_wanted = np.array([True,False,True])
print(array[rows_wanted,:])

#Broadcasting
#if arr2.shape is compatible to arr1.shape col it is brodcasted
arr1 = np.array([[2,1,5],[6,8,9]])
arr2 = np.array([5,4])
#(2, 3) (2,) can't compatible
#Either rows or columns shold be compatible
arr3 = np.array([1,5,7])
arr2 = np.array([[3],[5]])
print(arr1.shape,arr2.shape)
 
res1 = arr1+arr2
res2 = arr1 + arr3
print(res1,"\nsecond\n",res2)

# #Reshape to flatten
#Example 3: Flattening Arrays. You can convert an array of an unknown dimension to a 1D array using np.reshape(-1) 

arr1 = np.array([[1, 2, 3], [6, 7, 8], [4, 5, 6], [11, 14, 10]])
print("Original Array: \n", arr1, "\nShape: ", arr1.shape)

arr2 = np.reshape(arr1, (-1))
print("\nReshaped Array: \n", arr2, "\nShape: ", arr2.shape)
# Changing the dimension of array using reshape()
arr2 = np.resize(arr1, (5, 3))
print("Resized Array: \n", arr2, "\nShape: ", arr2.shape)

# Reshaping numpy array simply means changing the shape of the given array, shape basically tells the number of elements and dimension of array.
# By reshaping an array we can add or remove dimensions or change number of elements in each dimension.
# There are different ways that reshape numPy arrays:
# Changing the shape attribute (in-place operation)
# Use np.reshape() method (shallow copy)
# Use np.resize() method (deep copy)

# Use ndarray.transpose() method (shallow copy)
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Original Array: \n", arr1, "\nShape: ", arr1.shape)

#Reshape array using transpose method
arr2 = arr1.transpose()
print("\nTransposed array: \n", arr2,  "\nShape: ", arr2.shape)

## make change in one of the arrays, the change is reflected in both
arr2[1][1] = 99
print("\nOriginal Array: \n", arr1)
print("Transposed Array: \n", arr2)

# Use np.swapaxes()method (shallow copy)
# Use ndarray.flatten() method (deep copy)
