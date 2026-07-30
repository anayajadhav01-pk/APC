sentence = input("Enter a sentence: ")

words = sentence.split()

count = 0
for word in words:
    count += 1

print("Total number of words:", count)