class Shape:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print('Shape:', self.name)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Circle')
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__('Rectangle')
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__('Triangle')
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

c = Circle(5)
c.display_name()
print('Area:', c.area())

r = Rectangle(4, 6)
r.display_name()
print('Area:', r.area())

t = Triangle(3, 8)
t.display_name()
print('Area:', t.area())
