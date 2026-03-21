import pandas as pd 
df = pd.read_csv('sample.csv')
print(df,"\n")
print("\n", df.fillna(0)) # .fillna(0) method fills all the missing values with 0