import pandas as pd 
df = pd.read_csv('sample.csv')
print(df.dropna())
# here, dropna() drops all the rows because in every rows, every rows contain at least one nan values 