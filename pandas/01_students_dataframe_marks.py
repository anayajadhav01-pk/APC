import pandas as pd

data = {
    'Student ID': [101, 102, 103, 104, 105],
    'Student Name': ['Aarav', 'Diya', 'Rohan', 'Ananya', 'Ishaan'],
    'Python Marks': [85, 72, 92, 65, 78],
    'DBMS Marks': [90, 68, 88, 70, 82],
    'Mathematics Marks': [78, 75, 95, 60, 80]
}

df = pd.DataFrame(data)

df['Total Marks'] = df['Python Marks'] + df['DBMS Marks'] + df['Mathematics Marks']
df['Average Marks'] = df['Total Marks'] / 3

print('Students DataFrame:\n', df)
print('\nStudents with average marks > 75%:\n', df[df['Average Marks'] > 75])
