# Class methods and self example

class Student:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is " + self.name)

student1 = Student("Bakytzhan")
student1.say_hello()
