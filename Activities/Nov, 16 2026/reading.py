import json #Importing the JSON module

# Open and read a JSON file
with open('data.json', 'r') as file:
    info = json.load(file) # Load the JSON data from the file

print("Complete Employee Details:")
print(info)

print("\nFirst Employee Details:")
print(info["Employee Details"][0])

print("\nFirst Employee Name:")
print(info["Employee Details"][0]["emp_name"])

print("\nAll Employee Names:")
for employee in info["Employee Details"]:
    print(employee["emp_name"])