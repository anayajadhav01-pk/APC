from abc import ABC, abstractmethod

class Appointment(ABC):
    def __init__(self, patient_name):
        self.patient_name = patient_name

    @abstractmethod
    def book_appointment(self, slot_time):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass

class GeneralAppointment(Appointment):
    def book_appointment(self, slot_time):
        print(f'General consultation booked for {self.patient_name} at {slot_time}')

    def calculate_fee(self):
        return 300

class SpecialistAppointment(Appointment):
    def book_appointment(self, slot_time):
        print(f'Specialist consultation booked for {self.patient_name} at {slot_time}')

    def calculate_fee(self):
        return 1200

class EmergencyAppointment(Appointment):
    def book_appointment(self, slot_time):
        print(f'Emergency slot assigned immediately for {self.patient_name} (Priority triage)')

    def calculate_fee(self):
        return 2500

appointments = [
    GeneralAppointment('Ravi'),
    SpecialistAppointment('Meena'),
    EmergencyAppointment('Harish')
]

for appt in appointments:
    appt.book_appointment('10:30 AM')
    print('Consultation Fee: Rs.', appt.calculate_fee())
    print()
