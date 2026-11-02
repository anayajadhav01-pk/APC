class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

p1 = Product('Laptop', 65000)
p2 = Product('Desktop', 65000)
p3 = Product('Tablet', 30000)

print('p1 == p2:', p1 == p2)
print('p1 > p3:', p1 > p3)
print('p3 > p1:', p3 > p1)
