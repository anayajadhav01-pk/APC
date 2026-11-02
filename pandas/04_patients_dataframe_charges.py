import pandas as pd

data = {
    'Patient ID': [201, 202, 203, 204, 205],
    'Patient Name': ['Ramesh', 'Shanti', 'Manoj', 'Geeta', 'Suresh'],
    'Age': [65, 72, 45, 68, 38],
    'Disease': ['Diabetes', 'Hypertension', 'Fever', 'Arthritis', 'Asthma'],
    'Medical Charges': [45000, 55000, 12000, 62000, 28000]
}

df = pd.DataFrame(data)

print('Patients DataFrame:\n', df)
print('\nPatients above 60 years:\n', df[df['Age'] > 60])
print('\nAverage Medical Charge:', df['Medical Charges'].mean())
print('Maximum Medical Charge:', df['Medical Charges'].max())
print('\nPatients with Medical Charges > 50,000:\n', df[df['Medical Charges'] > 50000])
