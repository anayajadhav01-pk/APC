string = input("Enter a string: ")

freq = {}

for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

first = second = 0
first_char = second_char = ""

for ch in freq:
    if freq[ch] > first:
        second = first
        second_char = first_char
        first = freq[ch]
        first_char = ch
    elif freq[ch] > second and freq[ch] != first:
        second = freq[ch]
        second_char = ch

print("Second Most Frequent Character:", second_char)
print("Frequency:", second)