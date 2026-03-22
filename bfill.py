import pandas as pd 
df = pd.read_csv('sample.csv')
print(df,"\n")
print("\n", df.bfill())
"""bfill works as filling the nan value with the non missing value below. 
here, in row 7, name is missing, so, it is replaced by the data of below row. 
However, if there is no data below, like in row 10, it has no data to be replaced by
so, the data becomes still nan."""