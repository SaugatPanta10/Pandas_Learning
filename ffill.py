import pandas as pd 
df = pd.read_csv('sample.csv')
print(df,"\n")
print('\n', df.ffill())

"""  ffill works as filling the nan value with previous non missing value. 
here, in row 10, name is missing, so, it is replaced by the data of upper row. """