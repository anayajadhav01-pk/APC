from abc import ABC, abstractmethod

class FoodOrder(ABC):
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass

class RestaurantOrder(FoodOrder):
    def delivery_charge(self):
        return 0

    def calculate_bill(self):
        service_tax = 0.05 * (self.price * self.quantity)
        return (self.price * self.quantity) + service_tax + self.delivery_charge()

class HomeDeliveryOrder(FoodOrder):
    def delivery_charge(self):
        return 50

    def calculate_bill(self):
        gst = 0.05 * (self.price * self.quantity)
        return (self.price * self.quantity) + gst + self.delivery_charge()

ro = RestaurantOrder('Paneer Tikka', 250, 2)
hdo = HomeDeliveryOrder('Veg Biryani', 220, 3)

print('Dine-In Total Bill:', ro.calculate_bill())
print('Home Delivery Total Bill:', hdo.calculate_bill())
