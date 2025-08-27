
students = {
    "alice": "S12345",
    "bob": "S67890",
    "charlie": "S54321"
}


name_input = input("Enter student name: ").strip().lower()


student_id = students.get(name_input)

if student_id:
    print(f"The ID of {name_input.capitalize()} is {student_id}")
else:
    print(f"No student found with the name '{name_input}'")

print("Hi")