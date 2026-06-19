# Multiple inheritance example

class Father:
    def father_method(self):
        print("This is father method")

class Mother:
    def mother_method(self):
        print("This is mother method")

class Child(Father, Mother):
    pass

child1 = Child()
child1.father_method()
child1.mother_method()
