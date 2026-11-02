class Report:
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print('Generating PDF Report with charts and formatted tables.')

class ExcelReport(Report):
    def generate(self):
        print('Generating Excel Report with multi-sheet workbooks.')

class HTMLReport(Report):
    def generate(self):
        print('Generating HTML Report for web viewing.')

def print_report(report_obj):
    report_obj.generate()

reports = [PDFReport(), ExcelReport(), HTMLReport()]
for r in reports:
    print_report(r)
