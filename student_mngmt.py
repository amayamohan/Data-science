student_details = {101:"Aryan", 102:"Arjun", 103:"Amaya" , 104:"Nainu"}
print(student_details)

updated = student_details.update({101:"Virat"})
print("Updated student detail:" ,student_details)

student_details.pop(101)
print("After removed first element:" ,student_details)

for item, value in student_details.items():
  print(item ,":" ,value)


if 104 in student_details:
  print("Yes 104 is there")
else:
  print("No 104 is not there")

print("Total Number of students is the data base: ", len(student_details))


student_details.update({104:"Miya"})
print("Updated Student Record", student_details)  #append


#Accessing Item
access_item = student_details[102]
print(access_item)

print(student_details.keys())

print(student_details.values())

print(student_details.items())

for x in student_details:
    print(x)


for x in student_details.values():
    print(x)



