import pandas as pd
import numpy as np

data = {
    'Employee Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Alice', 'Frank', np.nan],
    'Age': [25, 30, 30, 40, np.nan, 25, 28, 35],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR', 'HR', 'IT', 'Finance'],
    'Salary ($)': [50000, 60000, 60000, 65000, 58000, 50000, 62000, 70000],
    'Joining Date': ['2020-01-10', '2019-03-15', '2019-03-15', '2018-07-20', '2021-05-12', '2020-01-10', '2020-10-01', '2022-01-01'],
    'Bonus %': [10, 15, 15, 20, np.nan, 10, 12, 18]
}

df = pd.DataFrame(data)
df.to_csv('ideal_dataframe.csv')