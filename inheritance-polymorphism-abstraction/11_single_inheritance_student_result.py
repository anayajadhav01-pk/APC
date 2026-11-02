class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

class Result(Student):
    def __init__(self, roll_no, name, course, m1, m2, m3):
        super().__init__(roll_no, name, course)
        self.marks = [m1, m2, m3]

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 3

    def grade(self):
        p = self.percentage()
        if p >= 80:
            return 'A'
        elif p >= 60:
            return 'B'
        elif p >= 40:
            return 'C'
        return 'F'

    def display_result(self):
        print('Roll No:', self.roll_no)
        print('Name:', self.name)
        print('Course:', self.course)
        print('Total:', self.total())
        print('Percentage:', self.percentage())
        print('Grade:', self.grade())

res = Result(105, 'Deepak', 'Computer Science', 82, 79, 91)
res.display_result()
