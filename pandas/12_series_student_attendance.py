import pandas as pd

attendance = {'Karan': 82.5, 'Pooja': 68.0, 'Rahul': 94.0, 'Simran': 71.5, 'Tanmay': 91.0}
s = pd.Series(attendance)

print('Attendance Series:\n', s)
print('\nAverage Attendance:', s.mean())
print('\nStudents with attendance below 75%:\n', s[s < 75])
print('\nStudents with attendance above 90%:\n', s[s > 90])
print('\nHighest Attendance:', s.idxmax(), 'with', s.max(), '%')
