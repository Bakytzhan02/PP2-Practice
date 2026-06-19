# Inheritance basics example

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is " + self.name)

class Student(Person):
    pass

student1 = Student("Bakytzhan")
student1.introduce()
