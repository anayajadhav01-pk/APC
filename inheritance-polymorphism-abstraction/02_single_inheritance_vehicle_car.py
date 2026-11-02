class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_vehicle(self):
        print('Brand:', self.brand)
        print('Model:', self.model)

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def discounted_price(self, discount_percent):
        return self.price - (self.price * (discount_percent / 100))

    def display_car(self):
        self.display_vehicle()
        print('Fuel Type:', self.fuel_type)
        print('Original Price:', self.price)
        print('Discounted Price (8% off):', self.discounted_price(8))

c = Car('Hyundai', 'Creta', 'Petrol', 1200000)
c.display_car()
