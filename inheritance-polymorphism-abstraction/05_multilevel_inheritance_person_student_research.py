class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print('Name:', self.name)
        print('Age:', self.age)

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def display_student(self):
        self.display_person()
        print('Roll Number:', self.roll_no)
        print('Course:', self.course)

class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide_name = guide_name

    def display_research_details(self):
        self.display_student()
        print('Research Topic:', self.topic)
        print('Guide Name:', self.guide_name)

rs = ResearchStudent('Neha Sen', 26, 'R-88', 'M.Tech', 'Neural Networks', 'Dr. Verma')
rs.display_research_details()
