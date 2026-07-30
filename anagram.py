string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if sorted(string1) == sorted(string2):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")