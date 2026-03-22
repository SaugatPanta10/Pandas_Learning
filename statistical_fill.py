import pandas as pd 
df = pd.read_csv('sample.csv')
print(df,"\n")
mean = df['Age'].mean()
print(mean)
df['Age'] = df['Age'].fillna(df['Age'].mean())
print("\n", "Updated table: ", "\n", df)

""" Here, the nan values of Age column are being replaced by the mean of all values of age"""