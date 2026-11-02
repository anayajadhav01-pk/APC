class Student:
    def __init__(self, name, total_marks):
        self.name = name
        self.total_marks = total_marks

    def __gt__(self, other):
        return self.total_marks > other.total_marks

    def __lt__(self, other):
        return self.total_marks < other.total_marks

s1 = Student('Vivek', 485)
s2 = Student('Ananya', 510)

print(f'{s1.name} Marks: {s1.total_marks}')
print(f'{s2.name} Marks: {s2.total_marks}')

if s1 > s2:
    print(f'{s1.name} scored more than {s2.name}')
elif s1 < s2:
    print(f'{s2.name} scored more than {s1.name}')
else:
    print('Both scored equal marks')
