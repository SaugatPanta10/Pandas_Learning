import pandas as pd 
df = pd.read_csv('sample.csv')
print(df,"\n")
new_df = df.duplicated()
print("\n", new_df)

""" .duplicated() shows if the data are duplicated. it returns the boolean value.
IMPORTANT NOTE: the data is duplicated if and only every columns of the particular row is same. 
for example : if the name only is duplicate, the data is not said to be duplicate, 
for a data to be duplicate , his age, salary, and everything should be duplicated.
row 1 and row 2 should be completely same to be duplicated data."""