try:
    marks = int(input("Enter student marks (0-100): "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    print("Student marks:", marks)

except ValueError as e:
    print("Exception:", e)

    





        











        








