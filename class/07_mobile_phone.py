class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specs(self):
        print('Brand:', self.brand)
        print('Model:', self.model)
        print('Storage:', self.storage)
        print('Original Price:', self.price)

    def discounted_price(self, discount_percent):
        discount = (discount_percent / 100) * self.price
        return self.price - discount

phone = MobilePhone('Samsung', 'Galaxy S23', '256GB', 75000)
phone.display_specs()
print('Price after 10% discount:', phone.discounted_price(10))
