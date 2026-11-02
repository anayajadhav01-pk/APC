class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print(f'Record initialized for {self.name}')

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        p = self.calculate_percentage()
        if p >= 85:
            return 'A'
        elif p >= 70:
            return 'B'
        elif p >= 50:
            return 'C'
        else:
            return 'Fail'

    def display(self):
        print('Student Name:', self.name)
        print('Total Marks:', self.calculate_total())
        print('Percentage:', self.calculate_percentage())
        print('Grade:', self.calculate_grade())

    def __del__(self):
        print(f'Result record for {self.name} cleared.')

res = StudentResult('Karan', [78, 85, 90, 72, 88])
res.display()
del res
