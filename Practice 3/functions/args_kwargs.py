# *args and **kwargs example

def show_subjects(*subjects):
    """This function accepts many positional arguments."""
    for subject in subjects:
        print(subject)

def show_student(**student):
    """This function accepts many keyword arguments."""
    print("Name:", student["name"])
    print("Course:", student["course"])

show_subjects("Python", "Git", "OOP")
show_student(name="Bakytzhan", course="PP2")
