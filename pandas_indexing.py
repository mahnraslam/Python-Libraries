import pandas as pd

df = pd.read_excel("titanic3.xls")
df = pd.DataFrame( df)

#Filtation
youngs = df[df["age"]<20]
 
# #For  saving
# df.to_csv("youngers.csv")

df2 = pd.read_csv("youngers.csv")

#Indexing or slicing
fourth_col = df2.iloc[:, 3]
#By labeling column
data  = df2.loc[4, ['name','home.dest']]
#Set index 
df2.set_index("pclass")
females = df2.loc[ (df2.age<15)]

#& for and | for or
boats = df2.loc[df2.body.notnull()]
df2["survived"] = "No"
print(df2["survived"])
#reviews['index_backwards'] = range(len(reviews), 0, -1)
#reviews['index_backwards']
 
#for returning first 3 rows
# print(df.head(3))
# students.loc[students['student_id'] == 101, ['name', 'age']]
#reviews.description.iloc[0]
#    reviews.description.iloc[:10]
# reviews.loc[[1,2,3,5,8]]