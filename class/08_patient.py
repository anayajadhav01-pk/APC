class Patient:
    def __init__(self, patient_id, name, age, disease, fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.fee = fee

    def display_info(self):
        print('Patient ID:', self.patient_id)
        print('Name:', self.name)
        print('Age:', self.age)
        print('Disease:', self.disease)
        print('Consultation Fee:', self.fee)

    def calculate_total_bill(self, medicine_charges, test_charges):
        return self.fee + medicine_charges + test_charges

p = Patient(201, 'Suresh Kumar', 45, 'Viral Fever', 500)
p.display_info()
print('Total Bill:', p.calculate_total_bill(1200, 800))
