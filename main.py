import salary

name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))

gross = salary.gross_salary(basic)
deduction = salary.deductions(gross)
net = salary.net_salary(gross, deduction)

print("\n--- Employee Salary Details ---")
print("Employee Name:", name)
print("Basic Salary:", basic)
print("Gross Salary:", gross)
print("Deductions:", deduction)
print("Net Salary:", net)