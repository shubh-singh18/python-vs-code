# Create a Student class with private __marks. Create a method that accepts marks only if they are between 0 and 100.
class Student:
    def __init__(self):
        self.__marks=0

    def set_marks(self,marks):
        if 0<=marks <=100:
            self.__marks=marks
        else:
            print("invalid marks")

    def display(self):
        print(self.__marks)

aa=Student()
aa.set_marks(78)
aa.display()
