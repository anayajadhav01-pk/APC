class Camera:
    def take_photo(self):
        print('Taking a high-resolution photo')

class Phone:
    def make_call(self, number):
        print(f'Calling {number}...')

class Smartphone(Camera, Phone):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f'Smartphone: {self.brand} {self.model}')

sp = Smartphone('Apple', 'iPhone 15')
sp.display()
sp.make_call('9876543210')
sp.take_photo()
