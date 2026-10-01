file = open("student1.txt", "r")

data = file.read()

file.close()

output = open("uppercase.txt", "w")

output.write(data.upper())

output.close()

print("Uppercase file created.")