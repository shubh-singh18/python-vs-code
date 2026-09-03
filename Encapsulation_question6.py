# Create an Employee class with private __salary. Create methods to set salary and display salary.
#  Salary should not be accessed directly outside the class.
class Employee:
    def __init__(self):
        self.__salary=0

    def set_salary(self,salary):
        self.__salary=salary

    def display(self):
        print(self.__salary)

a=Employee()
a.set_salary(3000)
a.display()