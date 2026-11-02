import pandas as pd

df = pd.read_csv('patients.csv')

print('Patients above 60 years:\n', df[df['Age'] > 60])
print('\nAverage Medical Expense:', df['Medical_Expense'].mean())

highest_patient = df.loc[df['Medical_Expense'].idxmax()]
print('\nPatient with highest medical expense:', highest_patient['Name'], 'at Rs.', highest_patient['Medical_Expense'])

print('\nPatient count for each disease:\n', df['Disease'].value_counts())
print('\nPatients whose medical expense exceeds Rs.50,000:\n', df[df['Medical_Expense'] > 50000])
