class Person:
    def __init__(self, name):
        self.name = name

    def display_role(self):
        pass

class Student(Person):
    def display_role(self):
        print(f'{self.name} is a Student attending lectures.')

class Faculty(Person):
    def display_role(self):
        print(f'{self.name} is a Faculty member delivering lectures and grading.')

class Administrator(Person):
    def display_role(self):
        print(f'{self.name} is an Administrator managing college operations.')

people = [
    Student('Aman'),
    Faculty('Prof. Kulkarni'),
    Administrator('Mr. Deshmukh')
]

for p in people:
    p.display_role()
