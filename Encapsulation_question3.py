# Create a Student class with a private variable __name. Set the name using a method and display it.
class Student:
    def __init__(self,):
        self.__name=""

    def set_name(self,name):
        self.__name=name

    def display(self):
       print(self.__name)

aa=Student()
aa.set_name("shubh")
aa.display()