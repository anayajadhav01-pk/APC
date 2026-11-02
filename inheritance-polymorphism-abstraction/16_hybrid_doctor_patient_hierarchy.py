class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

class Patient(Person):
    def __init__(self, name, age, ailment):
        super().__init__(name, age)
        self.ailment = ailment

class Surgeon(Doctor):
    def __init__(self, name, age, specialization, surgeries_count):
        super().__init__(name, age, specialization)
        self.surgeries_count = surgeries_count

class MedicalResearcher(Doctor):
    def __init__(self, name, age, specialization, publications):
        super().__init__(name, age, specialization)
        self.publications = publications

s = Surgeon('Dr. Mehta', 48, 'Cardiology', 250)
print(f'Surgeon: {s.name}, Age: {s.age}, Specialty: {s.specialization}, Surgeries: {s.surgeries_count}')

p = Patient('Ramesh', 35, 'Fracture')
print(f'Patient: {p.name}, Age: {p.age}, Ailment: {p.ailment}')
