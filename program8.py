file = open("student1.txt", "r")

lines = file.readlines()

for line in reversed(lines):
    print(line.strip())

file.close()