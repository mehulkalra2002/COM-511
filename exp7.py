# Creating a database using lists and tuples
# Each student record is represented as a tuple

# Database structure: (ID, Name, Age, Grade)
student_database = [
    (1, "Alice", 18, "A"),
    (2, "Bob", 19, "B"),
    (3, "Charlie", 17, "C"),
    (4, "David", 20, "A+")
]

# Function to retrieve student information by ID
def get_student_info(student_id):
    for record in student_database:
        if record[0] == student_id:
            return record
    return None

# Accessing and displaying student information
student_id_to_find = 3
found_student = get_student_info(student_id_to_find)

if found_student:
    print("Student found:")
    print("ID:", found_student[0])
    print("Name:", found_student[1])
    print("Age:", found_student[2])
    print("Grade:", found_student[3])
else:
    print("Student not found")
