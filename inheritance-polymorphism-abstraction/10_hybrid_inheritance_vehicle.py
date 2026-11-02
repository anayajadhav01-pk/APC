class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, num_doors):
        super().__init__(brand)
        self.num_doors = num_doors

class Bike(Vehicle):
    def __init__(self, brand, bike_type):
        super().__init__(brand)
        self.bike_type = bike_type

class SportsCar(Car):
    def __init__(self, brand, num_doors, top_speed):
        super().__init__(brand, num_doors)
        self.top_speed = top_speed

    def display(self):
        print(f'SportsCar: {self.brand}, Doors: {self.num_doors}, Top Speed: {self.top_speed} km/h')

class ElectricBike(Bike):
    def __init__(self, brand, bike_type, battery_capacity):
        super().__init__(brand, bike_type)
        self.battery_capacity = battery_capacity

    def display(self):
        print(f'ElectricBike: {self.brand}, Type: {self.bike_type}, Battery: {self.battery_capacity} kWh')

sc = SportsCar('Ferrari', 2, 340)
eb = ElectricBike('Revolt', 'Cruiser', 3.24)
sc.display()
eb.display()
