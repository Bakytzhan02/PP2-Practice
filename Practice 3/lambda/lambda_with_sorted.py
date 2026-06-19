# Lambda with sorted example

students = [("Ali", 85), ("Dana", 92), ("Bakytzhan", 78)]

sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)
