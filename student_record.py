student_records = {101: "Amaya"}

def AddRecord(roll_no, name):
    student_records[roll_no] = name
    print("Student record added:", roll_no, ":", name)

def UpdateRecord(roll_no, newName):
    if roll_no in student_records:
        student_records[roll_no] = newName
        print("Student record updated:", roll_no, ":", newName)
    else:
        print("Record not found")

def RemoveRecord(roll_no):
    if roll_no in student_records:
        del student_records[roll_no]
        print("Record removed for roll no:", roll_no)
    else:
        print("Record not found")

def viewRecord():
    print("Student Records:")
    for roll_no, name in student_records.items():
        print(roll_no, ":", name)

def lenRecord():
    print("Length of student records:", len(student_records))


print("Student Record Here....")
print("1: Add student record")
print("2: Update student record")
print("3: Remove student record")
print("4: View student record ")
print("5: Length of student record")
print("6: Exit")

choice = input("Enter your choice (1-6): ")
if choice == '1':
    roll_no = int(input("Enter roll number: "))
    name = input("Enter student name: ")
    AddRecord(roll_no, name)
elif choice == '2':
    roll_no = int(input("Enter roll number to update: "))
    newName = input("Enter new student name: ")
    UpdateRecord(roll_no, newName)
elif choice == '3':
    roll_no = int(input("Enter roll number to remove: "))
    RemoveRecord(roll_no)
elif choice == '4':
    viewRecord()
elif choice == '5':
    lenRecord()
elif choice == '6':
    print("Exit")
else:
    print("Invalid choice")