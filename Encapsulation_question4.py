# Create a Person class with a private variable __age. Create a method to set age and another method to display age.
class Person:
    def __init__(self,):
        self.__age=""

    def set_age(self,age):
        self.__age=age

    def display(self):
        print(self.__age)

aa=Person()
aa.set_age(30)
aa.display()