import pandas as pd 
df = pd.read_csv('sample.csv')
print(df.dropna(axis = 1)) # axis = 1 means column 
# here, in this case, only the first column is visible, because every other column contains at least one nan values 