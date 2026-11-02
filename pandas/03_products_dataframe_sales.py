import pandas as pd

data = {
    'Product ID': ['P1', 'P2', 'P3', 'P4', 'P5'],
    'Product Name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Printer'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics'],
    'Price': [55000, 500, 1200, 15000, 12000],
    'Quantity': [4, 25, 15, 6, 5]
}

df = pd.DataFrame(data)
df['Total Amount'] = df['Price'] * df['Quantity']

print('Products DataFrame:\n', df)
highest_product = df.loc[df['Total Amount'].idxmax()]
print('\nProduct having the highest total sales:\n', highest_product)
