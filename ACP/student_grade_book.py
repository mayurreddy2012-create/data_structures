
students = {"Mayur": 85,"Aarav": 92,"Riya": 78,"Sam": 90,"Neha": 88}
total = 0
for score in students.values():
    total += score
average = total / len(students)
print("Class average:", average)
highest = 0
for score in students.values():
    if score > highest:
        highest = score
print("Highest score:", highest)
name = input("Enter a student's name: ")
score = students.get(name)
if score is not None:
    print(name, "scored", score)
else:
    print("Student not found")