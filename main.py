from recursive import factorial, fibonacci, sum_of_digits, decimal_to_binary

n = int(input("Enter a number: "))

print("Factorial =", factorial(n))

print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")

print()

print("Sum of Digits =", sum_of_digits(n))

if n == 0:
    print("Binary =", 0)
else:
    print("Binary =", decimal_to_binary(n))