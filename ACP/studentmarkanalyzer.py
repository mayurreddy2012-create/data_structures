marks = [85, 72, 90, 68, 95, 80]
print("Number of students:", len(marks))
print("First student's marks:", marks[0])
print("Last student's marks:", marks[-1])
print("First three marks:", marks[:3])
print("Last three marks:", marks[-3:])
print("\nStudent Marks:")
for i in range(len(marks)):
    print("Student", i + 1, ":", marks[i])

total = sum(marks)
average = total / len(marks)
smallest = min(marks)
largest = max(marks)
print("\n----- Marks Summary -----")
print("Total Marks:", total)
print("Average Marks:", average)
print("Smallest Marks:", smallest)
print("Largest Marks:", largest)