with open ('students.txt,' 'w') as file:
    file.write("ID: 101, Name: abc, Grade: A, Major: Computer Science\n")
    file.write("ID: 102, Name: xyz, Grade: B, Major: Mathematics\n")
    file.write("ID: 103, Name: aaa, Grade: A, Major: Physics\n")
    file.write("ID: 104, Name: bbb, Grade: A+, Major: Chemistry\n")
    file.write("ID: 105, Name: ccc, Grade: B+, Major: Biology\n")

print ("--- Student Details from File ---")
with open('students.txt', 'r') as file:
    contents = file.read()
    print(contents)

