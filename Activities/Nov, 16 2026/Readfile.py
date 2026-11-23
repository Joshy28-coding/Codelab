#text file 'Readfile1.txt' with sample content
with open ('ReadFile1.txt', 'w') as f:
    f.write("Hello! This is the content of Readfile1.txt. \nSuccess! You have reached")

with open ('ReadFile1.txt') as file_handler:
    contents = file_handler.real()

print(contents)