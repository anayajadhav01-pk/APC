file = open("student1.txt", "r")

data = file.read()

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

data = data.replace(old_word, new_word)

file.close()

file = open("student1.txt", "w")

file.write(data)

file.close()

print("Word replaced successfully.")