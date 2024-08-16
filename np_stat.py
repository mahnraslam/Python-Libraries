import numpy as np
# np.sum	np.nansum	Compute sum of elements
# np.prod	np.nanprod	Compute product of elements
# np.mean	np.nanmean	Compute mean of elements
# np.std	np.nanstd	Compute standard deviation
# np.var	np.nanvar	Compute variance
# np.min	np.nanmin	Find minimum value
# np.max	np.nanmax	Find maximum value
# np.argmin	np.nanargmin	Find index of minimum value
# np.argmax	np.nanargmax	Find index of maximum value
# np.median	np.nanmedian	Compute median of elements
# np.percentile	np.nanpercentile	Compute rank-based statistics of elements
# np.any	N/A	Evaluate whether any elements are true
# np.all	N/A	Evaluate whether all elements are true

M = np.array([[2,3,45,2,4,1],[3,5,6,456,65,7],[5,6,4,64,7,8]])
# Player A: Mark scores at 24 and 26, with the mean at 25.
# Player B: Mark scores at 50 and 0, with the mean at 25.
a ,b = np.array([24,26]),np.array([50,0])
print(np.mean(a),np.mean(b))
print("A",np.std(a))
print("B",np.std(b))

'''
Player A is consistent with scores close to the mean.
Player B is inconsistent with scores far from the mean
Think of Player A as a student who gets similar marks in all exams, making their average predictable.
Think of Player B as a student who does extremely well in some exams and very poorly in others, making their average less predictable.
How to find consistency?
    Range: Smaller range indicates more consistency.  
    Range = max - min

    Variance: Lower variance indicates more consistency.
    Variance= ((24-25)**2 + (26-26)**2) // 2  = 1 while for b is 625

    Standard Deviation: Lower standard deviation indicates more consistency.
    std = np.sqrt(var)
    Standard Deviation= np.sqrt(625) =25

    Coefficient of Variation: Lower CV indicates more consistency.
    formula  CV= σ(std) / 𝜇(mean)
    a = 0.04 
    b = 25//25 equals to 1
1 
why there is a need of std when we have variance ?
Disadvantage of variance : Variance is in squared units of the original data, making it less interpretable in practical terms. For example, if the data is in meters, the variance will be in square meters.
That's why it is necessary to find the std.

2 why there is a need of CV equal to std//mean like 1//25 0.04 for player a
Coefficient of Variation (CV) is a useful measure to compare the relative variability of different datasets, particularly when the means are different.
 '''

# axis=0: This specifies the axis along which to find the minimum values.
# When axis=0 is specified, the function computes the minimum value for each column in a 2D array. Conversely, if axis=1 is specified, it would compute the minimum value for each row.
print(np.nanmin(M,axis = 1))
print(M.min())

import numpy as np

# Example data: heights of individuals in centimeters, with some NaN values
heights = np.array([160, 170, np.nan, 155, 180, 175, 168, 172, np.nan, 169])

# Calculate the 25th percentile, ignoring NaN values
percentile_25_nan = np.nanpercentile(heights, 25)
# print("25th percentile of heights, ignoring NaN values:", percentile_25_nan)
# np.concatenate(tup, axis=0)
# Where tup is comma separated ndarrays
# If axis is 0, it will join the arrays by row-wise (vertically). For 2-D arrays, the number of columns must match.
# If axis is 1, it will join the arrays by column-wise (horizontally). For 2-D arrays, the number of rows must match.
