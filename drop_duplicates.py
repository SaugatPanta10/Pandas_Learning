import pandas as pd 
df = pd.read_csv('sample.csv')
print(df,"\n")
new_df = df.drop_duplicates()
print("\n", new_df)

""" .drop_duplicates() removes the duplicated data. 
We have already learnt the duplicate data before."""