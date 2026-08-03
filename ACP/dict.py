# Student Subject Record Cleaner

# Step 1: Create a dictionary of student records
student_records = {
    "Mayur": "Math",
    "Aarav": "Science",
    "Diya": "English",
    "Riya": "History"
}

print("Original Records:")
print(student_records)

# Step 2: Access values safely
print("\nAccessing Records Safely:")
print("Mayur's subject:", student_records.get("Mayur"))
print("Rahul's subject:", student_records.get("Rahul", "Student not found"))

# Step 3: Add a new record
student_records["Rahul"] = "Computer Science"

# Step 4: Update an existing record
student_records["Diya"] = "Biology"

print("\nAfter Adding and Updating:")
print(student_records)

# Step 5: Remove an unwanted entry
student_records.pop("Riya")

print("\nAfter Removing Riya:")
print(student_records)

# Step 6: Check dictionary length
print("\nNumber of student records:", len(student_records))

# Step 7: Iterate through the final records
print("\nFinal Student Records:")
for student, subject in student_records.items():
    print(student, "->", subject)