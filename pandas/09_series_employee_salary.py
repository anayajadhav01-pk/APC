import pandas as pd

salaries = {'Rajesh': 65000, 'Priya': 48000, 'Vikram': 75000, 'Neha': 52000, 'Amit': 42000}
s = pd.Series(salaries)

print('Employee Salary Series:\n', s)
print('\nHighest Salary:', s.max())
print('Lowest Salary:', s.min())
print('Average Salary:', s.mean())
print('\nEmployees earning more than Rs.50,000:\n', s[s > 50000])
