string = input("Enter a string: ")

checked = ""

for ch in string:
    if ch not in checked:
        count = 0
        for c in string:
            if c == ch:
                count += 1
        print(ch, "=", count)
        checked += ch