string = input("Enter a string: ")

max_char = ""
max_count = 0

for ch in string:
    count = 0
    for c in string:
        if ch == c:
            count += 1
    if count > max_count:
        max_count = count
        max_char = ch

print("Most Frequent Character:", max_char)
print("Frequency:", max_count)