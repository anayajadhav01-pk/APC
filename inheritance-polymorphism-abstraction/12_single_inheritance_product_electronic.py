class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount_percent):
        return self.price - (self.price * (discount_percent / 100))

    def display(self):
        print('Product ID:', self.product_id)
        print('Name:', self.name)
        print('Brand:', self.brand)
        print('Warranty:', self.warranty)
        print('Original Price:', self.price)
        print('Final Price after 15% discount:', self.final_price(15))

ep = ElectronicProduct('E-909', 'Smart Television', 40000, 'Sony', '2 Years')
ep.display()
