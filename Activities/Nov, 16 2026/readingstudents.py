with open('students.txt', 'r') as file:
    file_content = file.read()

modified_contnet = file_content.replace(
    "ID: 102, Name: xyz, Grade: B, Major: Mathematics",
    "ID: 102, Name: xyz, Grade: A, Major: Mathematics"
)

with open ('students.txt', 'w') as file:
    file.write(modified_contnet)

print(" --- Updated Student Details --- ")
with open('students.txt', 'r') as file:
    print(file.read())