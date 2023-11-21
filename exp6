def create_student_record(id, name, age, grade):
    return {
        "ID": id,
        "Name": name,
        "Age": age,
        "Grade": grade
    }

def search_student(records, student_id):
    for record in records:
        if record["ID"] == student_id:
            return record
    return None

# Example records
student_records = [
    create_student_record(1, "Alice", 18, "A"),
    create_student_record(2, "Bob", 19, "B"),
    create_student_record(3, "Charlie", 17, "C"),
    create_student_record(4, "David", 20, "A+")
]

# Searching for a student by ID
search_id = 2
found_student = search_student(student_records, search_id)

if found_student:
    print("Student found:")
    print("ID:", found_student["ID"])
    print("Name:", found_student["Name"])
    print("Age:", found_student["Age"])
    print("Grade:", found_student["Grade"])
else:
    print("Student not found")
