class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return 0.20 * self.basic_salary

    def calculate_da(self):
        return 0.10 * self.basic_salary

    def calculate_gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    def display(self):
        print('Employee ID:', self.emp_id)
        print('Name:', self.name)
        print('Basic Salary:', self.basic_salary)
        print('HRA:', self.calculate_hra())
        print('DA:', self.calculate_da())
        print('Gross Salary:', self.calculate_gross_salary())

emp = Employee(1, 'John Doe', 50000)
emp.display()
