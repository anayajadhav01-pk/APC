from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print('Car engine started.')

    def stop(self):
        print('Car disc brakes applied. Engine stopped.')

class Bike(Vehicle):
    def start(self):
        print('Bike engine started with thumb start.')

    def stop(self):
        print('Bike brakes engaged. Bike parked.')

class Bus(Vehicle):
    def start(self):
        print('Bus air pressure built and engine started.')

    def stop(self):
        print('Bus air brakes applied and vehicle halted.')

vehicles = [Car(), Bike(), Bus()]
for v in vehicles:
    v.start()
    v.stop()
