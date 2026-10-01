def read_employees():
    file = open("employees.txt", "r")

    lines = file.readlines()

    file.close()

    employees = []

    for line in lines[1:]:
        id, name, department, salary = line.strip().split(",")

        employees.append({
            "ID": id,
            "Name": name,
            "Department": department,
            "Salary": float(salary)
        })

    return employees


def display_all(employees):
    for employee in employees:
        print(employee)


def highest_paid(employees):
    return max(employees, key=lambda x: x["Salary"])


def average_salary(employees):
    return sum(e["Salary"] for e in employees) / len(employees)


def above_salary(employees, amount):
    for employee in employees:
        if employee["Salary"] > amount:
            print(employee)


employees = read_employees()

print("All Employees:")
display_all(employees)

print("\nHighest Paid Employee:")
print(highest_paid(employees))

print("\nAverage Salary:")
print(average_salary(employees))

amount = float(input("\nEnter salary: "))

print("\nEmployees earning above given salary:")
above_salary(employees, amount)