class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = {}
        print(f'Shopping Cart {self.cart_id} created for {self.customer_name}')

    def add_product(self, name, price):
        self.products[name] = price
        print(f'Added {name}: {price}')

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print(f'Removed {name}')
        else:
            print(f'{name} not found in cart')

    def calculate_total(self):
        return sum(self.products.values())

    def __del__(self):
        print(f'Shopping Cart {self.cart_id} destroyed.')

cart = ShoppingCart('Anita Sharma', 'C-101')
cart.add_product('Book', 300)
cart.add_product('Pen', 50)
cart.add_product('Notebook', 100)
cart.remove_product('Pen')
print('Total Bill:', cart.calculate_total())
del cart
