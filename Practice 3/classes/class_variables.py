# Class variables and instance variables example

class Student:
    university = "SDU"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

student1 = Student("Bakytzhan")
student2 = Student("Ali")

print(student1.name)
print(student2.name)
print(student1.university)
print(student2.university)
