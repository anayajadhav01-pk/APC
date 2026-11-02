class Printer:
    def print_document(self, doc_name):
        print(f'Printing document: {doc_name}')

class Scanner:
    def scan_document(self, doc_name):
        print(f'Scanning document: {doc_name}')

class MultifunctionDevice(Printer, Scanner):
    def __init__(self, model):
        self.model = model

    def display_model(self):
        print(f'Multifunction Device: {self.model}')

mfd = MultifunctionDevice('HP LaserJet Pro MFP')
mfd.display_model()
mfd.print_document('Assignment.pdf')
mfd.scan_document('ID_Card.jpg')
