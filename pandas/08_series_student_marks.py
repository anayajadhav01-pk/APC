import pandas as pd

marks_dict = {'Aarav': 88, 'Diya': 72, 'Rohan': 95, 'Ananya': 68, 'Ishaan': 82}
s = pd.Series(marks_dict)

print('Student Marks Series:\n', s)
print('\nMarks of Rohan:', s['Rohan'])
print('Maximum Marks:', s.max())
print('Minimum Marks:', s.min())
print('Average Marks:', s.mean())
print('\nStudents with marks > 75:\n', s[s > 75])
