file = open("students.txt", "r")

lines = file.readlines()

file.close()

students = []

for line in lines[1:]:
    roll, name, marks = line.strip().split(",")

    students.append({
        "RollNo": roll,
        "Name": name,
        "Marks": int(marks)
    })

print("All Records:")

for student in students:
    print(student)

highest = max(students, key=lambda x: x["Marks"])

print("\nHighest Marks:")
print(highest)

average = sum(s["Marks"] for s in students) / len(students)

print("\nAverage Marks:", average)

print("\nStudents scoring more than 80:")

for student in students:
    if student["Marks"] > 80:
        print(student)