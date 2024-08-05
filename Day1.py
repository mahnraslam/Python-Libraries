import numpy as np
a = np.array([[10, 11, 12],
 [13, 14, 15],
 [16, 17, 18],
 [19, 20, 21],
 [22, 23, 24],
 [25, 26, 27],
 [28, 29, 30],
 [31, 32, 33]])
print("second row and first col",a[1,0])
# For Slicing
# x[start:stop:step]
print(a[3:5:1])
x = np.arange(12)
#Way to reverse
print(x[::-1])
print(x[:, 0])  # first column of x2

# Another useful type of operation is reshaping of arrays. The most flexible way of doing this is with the reshape method. For example, if you want to put the numbers 1 through 9 in a 3×3
#  grid, you can do the following:
x.reshape((3, 1))

# Concatenation of arrays
# Concatenation, or joining of two arrays in NumPy, is primarily accomplished using the routines np.concatenate,
# np.vstack, and np.hstack. np.concatenate takes a tuple or list of arrays as its first argument, as we can see here:
# no.vstack for column wise contatenation
# similarly split funtion works in  oppositeway and hsplit for dividing the rowsin equal  parts
left, right = np.hsplit(a, [2])
print(left)
print(right)
