from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass

class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2.5

class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 1.5 + 50

class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 15 + 100

class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 8.0 + 1500

dist = 120
transports = [Bus(), Train(), Taxi(), Flight()]
for t in transports:
    print(f'{t.__class__.__name__} Fare for {dist} km: Rs.{t.calculate_fare(dist)}')
