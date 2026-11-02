class Employee:
    def __init__(self, name, basic):
        self.name = name
        self.basic = basic

    def calculate_salary(self):
        return self.basic

class Manager(Employee):
    def calculate_salary(self):
        return self.basic + 20000

class Developer(Employee):
    def calculate_salary(self):
        return self.basic + 10000

class Tester(Employee):
    def calculate_salary(self):
        return self.basic + 6000

employees = [Manager('Arun', 60000), Developer('Sneha', 50000), Tester('Kunal', 40000)]
for e in employees:
    print(f'{e.name} ({e.__class__.__name__}) Salary: {e.calculate_salary()}')
