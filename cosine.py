x = float(input("Enter x (in radians): "))
n = int(input("Enter number of terms: "))

sum = 1
sign = -1

for i in range(2, n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j

    term = (x ** i) / fact
    sum = sum + sign * term
    sign = sign * -1

print("Cos(x) =", sum)