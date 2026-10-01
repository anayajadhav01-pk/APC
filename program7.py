file = open("student1.txt", "r")

data = file.read()

print("Total number of characters:", len(data))

file.close()