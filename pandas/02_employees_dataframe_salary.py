import pandas as pd

data = {
    'Employee ID': ['E01', 'E02', 'E03', 'E04', 'E05'],
    'Employee Name': ['Rajesh', 'Priya', 'Vikram', 'Neha', 'Amit'],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing'],
    'Salary': [65000, 48000, 75000, 52000, 42000],
    'Experience': [5, 3, 8, 4, 2]
}

df = pd.DataFrame(data)

print('Employees DataFrame:\n', df)
print('\nEmployees with Salary > 50,000:\n', df[df['Salary'] > 50000])
print('\nAverage Salary:', df['Salary'].mean())
print('Highest Salary:', df['Salary'].max())

max_exp_emp = df.loc[df['Experience'].idxmax()]
print('\nEmployee with highest experience:\n', max_exp_emp)
