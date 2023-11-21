# Function to add a student record to the list
def add_student(records, name, age, grade):
    records[name] = {'Age': age, 'Grade': grade}

# Function to search for a student record
def search_student(records, name):
    if name in records:
        return records[name]
    else:
        return "Student not found"

# Sample student records
student_records = {}

# Adding records to the list
add_student(student_records, 'Alice', 18, 'A')
add_student(student_records, 'Bob', 19, 'B')
add_student(student_records, 'Charlie', 20, 'C')

# Searching for a student record
search_name = 'Bob'
result = search_student(student_records, search_name)
if result != "Student not found":
    print(f"Student {search_name}'s record: Age - {result['Age']}, Grade - {result['Grade']}")
else:
    print(result)
