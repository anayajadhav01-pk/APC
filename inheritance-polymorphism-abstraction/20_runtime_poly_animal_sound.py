class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return 'Bark'

class Cat(Animal):
    def sound(self):
        return 'Meow'

class Cow(Animal):
    def sound(self):
        return 'Moo'

class Lion(Animal):
    def sound(self):
        return 'Roar'

animals = [Dog(), Cat(), Cow(), Lion()]
for a in animals:
    print(f'{a.__class__.__name__} says: {a.sound()}')
