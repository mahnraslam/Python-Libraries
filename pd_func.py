import pandas as pd 
import numpy as np
  
df = pd.read_csv("youngers.csv",  index_col=0)
 
#COUNT
c= df.groupby("age").age.count()
print("Show the type",type(c)
)
#idxmax
#Showing the maximum index from each group
df_groups = df.groupby("sex")
i  = df_groups.apply(lambda df_groups : df_groups.loc[df_groups.age.idxmax()])
print(i)

#Use of agg
# which lets you run a bunch of different functions on your DataFrame simultaneously.  
aggfuncs = [ 'count', 'sum', 'sem', 'skew', 'mean', 'min', 'max', 
'std', 'quantile', 'nunique', 'mad', 'size', pd.Series.mode, 'var', 'unique']
#With groupby
funcs =  df.groupby('name').agg(
    average_age=('age', 'mean'),
    highest_age=('age', 'max'),
    youngest=('age', 'min')
)
 
f = df.groupby(['name']).age.agg(['mean', 'max', 'min'])
print("3 funcs",f)
#Multiindex
 
f = df.groupby(["age"]).boat.agg([len]) 
#Sorting by len
print(type(f))

#Way to find the mean series
data  =  df.groupby(["name"]).age.agg(["mean"])
reviewer_mean_ratings = data['mean']
#2nd
data = df.groupby(["name"])['age'].mean().sort_index()
print(data)
f  = f.sort_values(by= ["age","len"]) 
print(f,type(f))
#USing agg with groupby


# Row indices and column labels separated into a list
df_indices = [pd.RangeIndex(start=0, stop=2, step=1), pd.Index(['col1', 'col2'], dtype='object')]

# Manually creating a DataFrame using these indices
df = pd.DataFrame([[10, 20], [30, 40]], index=df_indices[0], columns=df_indices[1])

#Apply fnun
df.apply(lambda x: x.sort_values(),axis= 1)

#Grouping and sorting

# Define a structured dtype with multiple fields
dtype = np.dtype([
    ('date', 'M8[D]'),  # Date with day precision
    ('value', 'f4'),    # 32-bit float
    ('label', 'S10')    # String of up to 10 bytes
])

# Create a DataFrame using this dtype
data = np.array([
    ('2024-08-01', 100.5, b'Example1'),
    ('2024-08-02', 200.0, b'Example2')
], dtype=dtype)
 

 
#by defaut the dispay.max_colwidth is 50 it can be change by pd.set_option("dispay.max_colwidth",1000
'''
Coubt desc if it contains desired word
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
For counting word
fruity_counts = reviews.description.map(lambda p : p.count("tropical")).sum()
topical_counts = reviews.description.map(lambda p : p.count("fruity")).sum()
descriptor_counts =  pd.Series(data =[topical_counts, fruity_counts] , index = ["tropical","fruity"]) 
'''