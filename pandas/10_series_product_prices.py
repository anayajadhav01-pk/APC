import pandas as pd

prices = {'Book': 450, 'Pen': 80, 'Headphones': 1800, 'Backpack': 1500, 'Watch': 3200}
s = pd.Series(prices)

print('All Products and Prices:\n', s)

s_increased = s * 1.10
print('\nPrices after 10% increase:\n', s_increased)

print('\nMost expensive product:', s.idxmax(), 'at Rs.', s.max())
print('\nProducts costing more than Rs.1,000:\n', s[s > 1000])
