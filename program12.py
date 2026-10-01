file = open("student1.txt", "r")

data = file.read().lower()

words = data.split()

count = {}

for word in words:
    word = word.strip(".,!?")

    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)

file.close()