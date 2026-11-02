import pandas as pd

data = {
    'Product_ID': [101, 102, 103, 104, 105],
    'Product_Name': ['Rice Bag', 'Wheat Flour', 'Olive Oil', 'Sugar Bag', 'Tea Packets'],
    'Category': ['Grocery', 'Grocery', 'Grocery', 'Grocery', 'Beverage'],
    'Price': [1200, 450, 800, 1800, 250],
    'Quantity': [15, 30, 8, 10, 40]
}

df = pd.DataFrame(data)
df['Total_Sales'] = df['Price'] * df['Quantity']

print('Retail Sales DataFrame:\n', df)
print('\nProducts with sales > Rs.10,000:\n', df[df['Total_Sales'] > 10000])
print('\nProduct with maximum sales:\n', df.loc[df['Total_Sales'].idxmax()])
print('\nAverage Sales:', df['Total_Sales'].mean())
