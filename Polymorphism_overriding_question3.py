# Create a Person class with a display() method. Create a Student class that overrides display() and displays student details
class Person:
    def display(self):
        print("student name is devansh")
class Student(Person):
    def display(self):
        print("studdent name is shivam")
aa=Student()
aa.display()
        