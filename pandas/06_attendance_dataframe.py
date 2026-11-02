import pandas as pd

data = {
    'Student_ID': [1, 2, 3, 4, 5],
    'Name': ['Karan', 'Pooja', 'Rahul', 'Simran', 'Tanmay'],
    'Department': ['CSE', 'IT', 'CSE', 'ECE', 'CSE'],
    'Total_Classes': [60, 60, 60, 60, 60],
    'Classes_Attended': [52, 40, 58, 39, 48]
}

df = pd.DataFrame(data)
df['Attendance Percentage'] = (df['Classes_Attended'] / df['Total_Classes']) * 100

print('Attendance DataFrame:\n', df)
print('\nStudents whose attendance is below 75%:\n', df[df['Attendance Percentage'] < 75])
