class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def get_percentage(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print('Roll No:', self.roll_no)
        print('Name:', self.name)
        print('Marks:', self.marks)
        print('Percentage:', self.get_percentage())
        print()

s1 = Student(101, 'Rahul', [85, 90, 78])
s2 = Student(102, 'Priya', [92, 88, 95])
s3 = Student(103, 'Amit', [70, 75, 80])

s1.display()
s2.display()
s3.display()
