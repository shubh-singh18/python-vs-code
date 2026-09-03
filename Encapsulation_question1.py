# Create a Student class with a private variable __marks. Create methods to set and display marks.
class Student:
    def __init__(self):
        self.__marks=78
    def set_marks(self,marks):
        self.__marks=marks
    
    def display(self):
        print(self.__marks)
aa=Student()
aa.set_marks(85)
aa.display()     