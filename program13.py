file = open("student1.txt", "r")

search = input("Enter word to search: ").lower()

count = 0
line_numbers = []

for number, line in enumerate(file, start=1):
    words = line.lower().split()

    if search in words:
        count += words.count(search)
        line_numbers.append(number)

print("Occurrences:", count)
print("Line numbers:", line_numbers)

file.close()