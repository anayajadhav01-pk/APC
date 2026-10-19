def total(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / len(marks)

def grade(per):
    if per >= 90:
        return "A"
    elif per >= 75:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 40:
        return "D"
    else:
        return "Fail"

marks = list(map(int, input("Enter marks of 5 subjects: ").split()))

t = total(marks)
p = percentage(marks)
g = grade(p)

print("Total Marks:", t)
print("Percentage:", p, "%")
print("Grade:", g)
