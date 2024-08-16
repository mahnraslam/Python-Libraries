import numpy as np
# The only required argument is name of file, and by default the numbers are casted to float data type
#Withiut missing value...So using loadtxt'
#numpy.loadtxt can be used to load data from a CSV file, but it has some limitations. The function is designed to work with simple text files where each row has the same number of values, and all values are of the same data type (usually numeric). It is not as flexible as pandas.read_csv for handling complex CSV files.
 
# Load data as a float array
arr = np.loadtxt("myarr.txt", delimiter=' ', comments="#", dtype=np.float64)
#HOW TO CHANGE THE DATA TYPE
# Convert the array to an integer type
arr_int = arr.astype(np.int64)

# Convert the array to a different type, e.g., float32
arr_float32 = arr.astype(np.float32)

 
#IN case data has missing use genfromtxt
#filling_values  use to fill the empty spaces 
 
# Load the data from the file
arr = np.genfromtxt("my_arr.txt", dtype=np.int64, delimiter='\t', skip_header=0, comments='#', filling_values=0)

print(arr)

 
 