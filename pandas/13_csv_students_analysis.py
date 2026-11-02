import pandas as pd

df = pd.read_csv('students.csv')

print('First 5 records:\n', df.head())
print('\nLast 5 records:\n', df.tail())

df['Total'] = df['Python'] + df['DBMS'] + df['Maths']
df['Average'] = df['Total'] / 3

print('\nTotal and Average Marks for each student:\n', df[['Student_ID', 'Name', 'Total', 'Average']])
print('\nStudents with average marks > 75:\n', df[df['Average'] > 75])

top_student = df.loc[df['Average'].idxmax()]
print('\nStudent with highest average:\n', top_student['Name'], 'with', top_student['Average'])

print('\nAverage marks for each subject:')
print('Python:', df['Python'].mean())
print('DBMS:', df['DBMS'].mean())
print('Maths:', df['Maths'].mean())
