# Practice 4 - JSON Parsing and Creation

import json

# 1. Parsing JSON string to Python dictionary
student_json = '{"name": "Bakytzhan", "age": 18, "course": "PP2"}'
student_data = json.loads(student_json)

print(student_data)
print(student_data["name"])

# 2. Converting Python dictionary to JSON string
student = {
    "name": "Bakytzhan",
    "age": 18,
    "course": "PP2",
    "topics": ["Python", "JSON", "Math"]
}

json_string = json.dumps(student, indent=4)
print(json_string)

# 3. Writing JSON data to a file
with open("student-data.json", "w") as file:
    json.dump(student, file, indent=4)

# 4. Reading JSON data from a file
with open("student-data.json", "r") as file:
    loaded_student = json.load(file)

print("Loaded student:", loaded_student)

# 5. Working with sample-data.json
with open("sample-data.json", "r") as file:
    sample_data = json.load(file)

print("Students from sample-data.json:")
for item in sample_data["students"]:
    print(item["name"], "-", item["course"])
