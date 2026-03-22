import pandas as pd 
df = pd.read_csv('sample.csv')
print(df,"\n")
print("\n", df.dropna(subset = ['Remarks'])) 
# this removes rows where the given column has nan values . here, remarks had nan values in row with 10th index, so, it removed that row