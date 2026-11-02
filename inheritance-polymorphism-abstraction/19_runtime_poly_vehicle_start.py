class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print('Car starts with key ignition or start button.')

class Bike(Vehicle):
    def start(self):
        print('Bike starts with self-start button or kick.')

class Bus(Vehicle):
    def start(self):
        print('Bus starts with heavy diesel ignition engine.')

fleet = [Car(), Bike(), Bus()]
for v in fleet:
    v.start()
