from mathutils.basic import add, subtract, multiply, divide
from mathutils.number import is_prime, is_armstrong, is_palindrome
from mathutils.statistics import mean, maximum, minimum

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\n--- Arithmetic Operations ---")
print("Addition =", add(a, b))
print("Subtraction =", subtract(a, b))
print("Multiplication =", multiply(a, b))
print("Division =", divide(a, b))

n = int(input("\nEnter a number to check: "))

print("\n--- Number Operations ---")

if is_prime(n):
    print("Prime: Yes")
else:
    print("Prime: No")

if is_armstrong(n):
    print("Armstrong: Yes")
else:
    print("Armstrong: No")

if is_palindrome(n):
    print("Palindrome: Yes")
else:
    print("Palindrome: No")

numbers = [10, 20, 30, 40, 50]

print("\n--- Statistics ---")
print("Mean =", mean(numbers))
print("Maximum =", maximum(numbers))
print("Minimum =", minimum(numbers))