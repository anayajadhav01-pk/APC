import pandas as pd

ages = {101: 45, 102: 67, 103: 72, 104: 34, 105: 62, 106: 28}
s = pd.Series(ages)

print('Patient Ages Series (Index: Patient ID):\n', s)
print('\nAverage Age:', s.mean())
print('Oldest Patient ID:', s.idxmax(), 'Age:', s.max())
print('Youngest Patient ID:', s.idxmin(), 'Age:', s.min())
print('\nPatients above 60 years:\n', s[s > 60])
