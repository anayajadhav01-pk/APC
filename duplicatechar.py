string = input("Enter a string: ")

printed = ""

print("Duplicate characters are:")

for i in range(len(string)):
    count = 0
    for j in range(len(string)):
        if string[i] == string[j]:
            count += 1

    if count > 1 and string[i] not in printed:
        print(string[i])
        printed += string[i]