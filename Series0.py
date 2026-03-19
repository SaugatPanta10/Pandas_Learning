""" a seies is like a column in  a table 
it is a one dimensional array holding data of any type. 
"""

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

df = pd.Series(calories)
print(df)
print(df["day1"])