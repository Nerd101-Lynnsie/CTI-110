###Practicing Dictionaries in Python
###Create a dictionary
students = {101:"Trey", 321:"Ray", 638:"AJ"}
print()

###Print a value using the established keys
print(students[321])

###Show all keys in the dictionary
print(students.keys())
print(students.values())

###Add a new key:value pair to the dictionary
students[222] = "Gerald"

print(students)

###Add a new student - user gives info
new_student_id = int(input("Enter a new student ID: "))
print()
new_student_name = input("Enter the new student name: ")

###Officially add new student to dictionary
students[new_student_id] = new_student_name
print()
print(students)

###REMOVE item from dictionary
students.pop(101)
print()
print(students)
