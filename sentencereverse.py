sentence = input("Enter a sentence: ")

words = sentence.split()

reverse = words[::-1]

print("Reversed Sentence:", " ".join(reverse))