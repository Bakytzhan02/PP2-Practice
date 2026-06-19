# super() function example

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

student1 = Student("Bakytzhan", "PP2")

print(student1.name)
print(student1.course)
