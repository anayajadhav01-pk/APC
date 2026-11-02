class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            return self.units * 3.0
        elif self.units <= 200:
            return (100 * 3.0) + (self.units - 100) * 4.5
        elif self.units <= 300:
            return (100 * 3.0) + (100 * 4.5) + (self.units - 200) * 6.0
        else:
            return (100 * 3.0) + (100 * 4.5) + (100 * 6.0) + (self.units - 300) * 8.0

    def display(self):
        print('Consumer Number:', self.consumer_no)
        print('Consumer Name:', self.consumer_name)
        print('Units Consumed:', self.units)
        print('Total Bill: Rs.', self.calculate_bill())

bill = ElectricityBill(1001, 'Ramesh', 250)
bill.display()
