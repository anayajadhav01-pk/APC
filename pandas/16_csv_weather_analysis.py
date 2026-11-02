import pandas as pd

df = pd.read_csv('weather.csv')

print('Maximum Temperature:', df['Temperature'].max())
print('Minimum Temperature:', df['Temperature'].min())
print('Average Temperature:', df['Temperature'].mean())
print('\nRecords where Temperature is above 35°C:\n', df[df['Temperature'] > 35])
print('\nCity-wise Average Temperature:\n', df.groupby('City')['Temperature'].mean())
