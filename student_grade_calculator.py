name=input("Enter student name: ")

m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

total = m1 + m2 + m3
avg = total/3

if avg >= 80 and avg <= 100:
    grade="A+"
elif avg >= 70 and avg < 80:
    grade="A"
elif avg >= 60 and avg < 70:
    grade="B"
elif avg >= 50 and avg < 60:
    grade="C"
else:
    grade="F"

print(f"\nStudent Name: {name}")
print(f"Total Marks: {total:.0f}")
print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")