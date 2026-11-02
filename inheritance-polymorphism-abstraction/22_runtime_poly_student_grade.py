class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        pass

class EngineeringStudent(Student):
    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks)
        return 'A (Distinction)' if avg >= 75 else 'B'

class MedicalStudent(Student):
    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks)
        return 'Honors' if avg >= 80 else 'Pass'

class ManagementStudent(Student):
    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks)
        return 'Grade 1' if avg >= 70 else 'Grade 2'

students = [
    EngineeringStudent('Rohan', [78, 82, 80]),
    MedicalStudent('Shreya', [85, 88, 90]),
    ManagementStudent('Tanmay', [72, 74, 68])
]

for s in students:
    print(f'{s.name} ({s.__class__.__name__}) Grade: {s.calculate_grade()}')
