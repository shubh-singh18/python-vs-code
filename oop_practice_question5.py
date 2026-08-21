# Create a Person class with a constructor. Create a Student class that uses super() to call the parent constructor.
class Person:
    def __init__(self):
        print("this is a person class")
class Student(Person):
    def __init__(self):
        super(). __init__()
aa=Student()




