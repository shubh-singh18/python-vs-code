#create a Employee class with name and salary.create a manager class that inherits from employee.
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def display(self):
        print(self.name,self.salary)
aa=manager("divansh",50000)
aa.display()