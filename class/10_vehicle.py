class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.is_available = True

    def rent_vehicle(self, days):
        if self.is_available:
            self.is_available = False
            cost = days * self.rental_rate
            print(f'Vehicle {self.model} rented for {days} days. Total charges: {cost}')
        else:
            print(f'Vehicle {self.model} is currently not available.')

    def return_vehicle(self):
        self.is_available = True
        print(f'Vehicle {self.model} returned successfully.')

v = Vehicle('MH12-AB-9999', 'Sedan Car', 1500)
v.rent_vehicle(4)
v.rent_vehicle(2)
v.return_vehicle()
v.rent_vehicle(2)
