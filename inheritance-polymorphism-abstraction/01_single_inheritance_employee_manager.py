class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_employee(self):
        print('Employee ID:', self.emp_id)
        print('Name:', self.name)
        print('Monthly Salary:', self.salary)

class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def annual_salary(self):
        return self.salary * 12

    def display_manager(self):
        self.display_employee()
        print('Department:', self.department)
        print('Annual Salary:', self.annual_salary())

m = Manager(101, 'Sunil Sharma', 60000, 'Operations')
m.display_manager()
