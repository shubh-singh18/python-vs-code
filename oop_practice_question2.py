# Create an Employee class with name and salary. Create a Manager class that inherits from Employee and adds department
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def __init__(self,name,salary,addsdepartment):
        super().__init__(name,salary)
        self.addsdepartment=addsdepartment

    def display(self):
        print(self.name)
        print(self.salary)
        print(self.addsdepartment)

s=Manager("shivam","50000","CSE")
s.display()



