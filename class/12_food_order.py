class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price
        print(f'Order {self.order_id} placed by {self.customer_name}')

    def calculate_total_bill(self, tax_percent=5):
        subtotal = self.quantity * self.price
        tax = (tax_percent / 100) * subtotal
        return subtotal + tax

    def __del__(self):
        print(f'Order {self.order_id} completed and closed.')

order = FoodOrder('ORD-555', 'Manish', 'Pizza', 2, 350)
print('Total Bill with Tax:', order.calculate_total_bill(5))
del order
