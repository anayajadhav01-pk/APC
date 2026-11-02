class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def display_base(self):
        print(f'{self.name} (ID: {self.emp_id}) - Basic: {self.basic_salary}')

class Manager(Employee):
    def calculate_salary(self):
        allowance = 15000
        return self.basic_salary + allowance

class Developer(Employee):
    def calculate_salary(self):
        allowance = 8000
        return self.basic_salary + allowance

class Tester(Employee):
    def calculate_salary(self):
        allowance = 5000
        return self.basic_salary + allowance

m = Manager(1, 'Aakash', 70000)
d = Developer(2, 'Pooja', 50000)
t = Tester(3, 'Rohan', 40000)

m.display_base()
print('Manager Net Salary:', m.calculate_salary())
d.display_base()
print('Developer Net Salary:', d.calculate_salary())
t.display_base()
print('Tester Net Salary:', t.calculate_salary())
