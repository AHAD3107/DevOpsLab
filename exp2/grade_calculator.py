name = input("Enter Student Name: ")
marks = float(input("Enter Marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print("\nStudent Name:", name)
print("Marks:", marks)
print("Grade:", grade)