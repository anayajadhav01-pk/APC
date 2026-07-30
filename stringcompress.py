string = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(string)):
    if i < len(string)-1 and string[i] == string[i+1]:
        count += 1
    else:
        compressed += string[i] + str(count)
        count = 1

if len(compressed) < len(string):
    print("Compressed String:", compressed)
else:
    print("Original String:", string)