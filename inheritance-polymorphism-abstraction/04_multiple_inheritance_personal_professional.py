class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_personal(self):
        print('Name:', self.name)
        print('Age:', self.age)

class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary

    def display_professional(self):
        print('Employee ID:', self.emp_id)
        print('Designation:', self.designation)
        print('Salary:', self.salary)

class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display_complete_info(self):
        self.display_personal()
        self.display_professional()

emp = Employee('Vikram Rao', 32, 'EMP-502', 'Data Analyst', 75000)
emp.display_complete_info()
