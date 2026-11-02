class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating.')

class Dog(Animal):
    def sound(self):
        print(f'{self.name} barks: Woof Woof!')

class Cat(Animal):
    def sound(self):
        print(f'{self.name} meows: Meow Meow!')

class Cow(Animal):
    def sound(self):
        print(f'{self.name} moos: Moo Moo!')

d = Dog('Tommy')
c = Cat('Kitty')
w = Cow('Gauri')

d.eat()
d.sound()
c.sound()
w.sound()
