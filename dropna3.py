import pandas as pd 
df = pd.read_csv('sample.csv')
print(df,"\n")
print("\n",df.dropna(how = 'all')) 
"""this will remove those rows containing all values nan. 
however, there is no any rows containing all values nan. so, it returns the same table"""