class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
        self.normalize()

    def normalize(self):
        if self.inches >= 12:
            self.feet += self.inches // 12
            self.inches = self.inches % 12

    def __add__(self, other):
        total_feet = self.feet + other.feet
        total_inches = self.inches + other.inches
        return Distance(total_feet, total_inches)

    def display(self):
        print(f'{self.feet} feet {self.inches} inches')

d1 = Distance(5, 9)
d2 = Distance(3, 7)
d3 = d1 + d2

print('Distance 1: ', end='')
d1.display()
print('Distance 2: ', end='')
d2.display()
print('Total Distance: ', end='')
d3.display()
