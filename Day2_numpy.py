#  It takes several seconds to compute these million operations and to store the result! When even cell phones have processing speeds measured in Giga-FLOPS (i.e., billions of numerical operations per second)

# For many types of operations, NumPy provides a convenient interface into just this kind of statically typed, compiled routine. This is known as a vectorized operation. This can be accomplished by simply performing an operation on the array, which will then be applied to each element. This vectorized approach is designed to push the loop into the compiled layer that underlies NumPy, leading to much faster execution.
import numpy as np
 
 
print(np.arange(5) / np.arange(1, 6))

# Ufuncs exist in two flavors: unary ufuncs, which operate on a single input, and binary ufuncs, which operate on two inputs. We'll see examples of both these types of functions here.
x = np.arange(5)
# print("x     =", x)
# print("x + 5 =", x + 5)
# print("x - 5 =", x - 5)
# print("x * 2 =", x * 2)
# print("x / 2 =", x / 2)
# print("x // 2 =", x // 2)  # floor division

y = np.empty(5)
np.multiply(x, 10, out= y)
res = x*10
print(y,res)

#  A reduce repeatedly applies a given operation to the elements of an array until only a single result remains.
# For example, calling reduce on the add ufunc returns the sum of all elements in the array:
print(np.add.reduce(x))
print(np.multiply.reduce(x))
#If we'd like to store all the intermediate results of the computation, we can instead use accumulate:
print(np.add.accumulate(x))
# Finally, any ufunc can compute the output
# of all pairs of two different inputs using the outer method. This allows you, in one line, to do things like create a multiplication table:
np.multiply.outer(x,x)
 