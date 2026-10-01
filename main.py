from string_utils import count_vowels, reverse_string, is_palindrome, count_words, remove_spaces

text = input("Enter a string: ")

print("Number of vowels:", count_vowels(text))
print("Reverse:", reverse_string(text))
print("Palindrome:", is_palindrome(text))
print("Number of words:", count_words(text))
print("Without spaces:", remove_spaces(text))