from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass

class InPatient(Patient):
    def __init__(self, name, days, room_rate):
        super().__init__(name)
        self.days = days
        self.room_rate = room_rate

    def treatment(self):
        print(f'{self.name} admitted in hospital under observation.')

    def calculate_bill(self):
        return self.days * self.room_rate + 2000

class OutPatient(Patient):
    def __init__(self, name, consultation_fee):
        super().__init__(name)
        self.consultation_fee = consultation_fee

    def treatment(self):
        print(f'{self.name} consulted doctor in OPD.')

    def calculate_bill(self):
        return self.consultation_fee + 300

class EmergencyPatient(Patient):
    def __init__(self, name, icu_charge):
        super().__init__(name)
        self.icu_charge = icu_charge

    def treatment(self):
        print(f'{self.name} received immediate trauma care.')

    def calculate_bill(self):
        return self.icu_charge + 5000

patients = [InPatient('Manoj', 4, 1500), OutPatient('Sarita', 500), EmergencyPatient('Gopal', 12000)]
for p in patients:
    p.treatment()
    print('Bill Amount: Rs.', p.calculate_bill())
