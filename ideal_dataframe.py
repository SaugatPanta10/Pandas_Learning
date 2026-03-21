import pandas as pd
import numpy as np

data = {
    'Employee Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Alice', 'Frank', np.nan, 'George', 'Hannah', np.nan],
    'Age': [25, 30, 30, 40, np.nan, 25, 28, 35, np.nan, 29, np.nan],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR', 'HR', 'IT', 'Finance', 'Finance', 'IT', np.nan],
    'Salary ($)': [50000, 60000, 60000, 65000, 58000, 50000, 62000, 70000, np.nan, 59000, np.nan],
    'Joining Date': ['2020-01-10', '2019-03-15', '2019-03-15', '2018-07-20', '2021-05-12',
                     '2020-01-10', '2020-10-01', '2022-01-01', '2021-06-18', np.nan, np.nan],
    'Bonus %': [10, 15, 15, 20, np.nan, 10, 12, 18, 15, np.nan, np.nan],
    'Status': ['Active', 'Inactive', 'Inactive', 'Active', 'Active', 'Active', 'Inactive', 'Active', 'Active', 'Inactive', np.nan],
    'Remarks': ['Good', 'Average', 'Average', np.nan, 'Excellent', 'Good', 'Average', 'Excellent', 'Poor', 'Good', np.nan],
    'Empty Column': [np.nan]*11,  # completely empty column to test column drop
    'Completely Empty Row': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]  # one fully empty row
}

df = pd.DataFrame(data)
print(df)