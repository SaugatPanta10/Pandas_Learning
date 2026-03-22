import pandas as pd 
df = pd.read_csv('sample.csv')
print(df,"\n")
new_df = df.duplicated()
print("\n", new_df)

""" .duplicated() shows if the data are duplicated. it returns the boolean value.
IMPORTANT NOTE: the data is duplicated if and only every columns of the particular data is same. 
for example : row 1 and row 2 should be completely same to be duplicated data."""