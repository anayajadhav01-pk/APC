class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

class Faculty(Person):
    def __init__(self, name, age, faculty_id):
        super().__init__(name, age)
        self.faculty_id = faculty_id

class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, student_id, faculty_id, subject):
        Person.__init__(self, name, age)
        self.student_id = student_id
        self.faculty_id = faculty_id
        self.subject = subject

    def display(self):
        print('TA Name:', self.name)
        print('Age:', self.age)
        print('Student ID:', self.student_id)
        print('Faculty ID:', self.faculty_id)
        print('Subject:', self.subject)

ta = TeachingAssistant('Kavita', 24, 'S-201', 'FAC-404', 'Machine Learning')
ta.display()
