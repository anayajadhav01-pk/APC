class Academic:
    def __init__(self, marks):
        self.marks = marks

    def get_academic_score(self):
        return sum(self.marks) / len(self.marks)

class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points

    def get_sports_score(self):
        return self.sports_points

class Student(Academic, Sports):
    def __init__(self, name, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)
        self.name = name

    def display_overall_performance(self):
        acad = self.get_academic_score()
        sports = self.get_sports_score()
        overall = (acad * 0.7) + (sports * 0.3)
        print('Student Name:', self.name)
        print('Academic Average:', acad)
        print('Sports Points:', sports)
        print('Overall Score:', overall)

s = Student('Anjali', [88, 92, 85], 80)
s.display_overall_performance()
