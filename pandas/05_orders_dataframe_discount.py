import pandas as pd

data = {
    'Order_ID': ['O101', 'O102', 'O103', 'O104', 'O105'],
    'Customer': ['Arun', 'Bina', 'Chirag', 'Deepa', 'Eshwar'],
    'Product': ['Shoes', 'Watch', 'Headphones', 'Tablet', 'Backpack'],
    'Quantity': [2, 1, 3, 1, 2],
    'Price': [2500, 4500, 1500, 18000, 1200],
    'Discount': [300, 500, 200, 1500, 100]
}

df = pd.DataFrame(data)
df['Final Amount'] = (df['Quantity'] * df['Price']) - df['Discount']

print('All Orders:\n', df)
print('\nOrders above Rs.5,000:\n', df[df['Final Amount'] > 5000])
print('\nHighest-value order:\n', df.loc[df['Final Amount'].idxmax()])
print('\nAverage order value:', df['Final Amount'].mean())
