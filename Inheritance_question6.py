# create Person->employee->->manager->classess.Add different attributes at each level and display them.
class Person:
    def __init__(self,name):
        self.name=name
class Employee(Person):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary
class manager(Employee):
    def __init__(self,name,salary,section):
        super().__init__(name,salary)
        self.section=section

    def display(self):
        print(self.name)
        print(self.salary)
        print(self.section)
aa=manager("devansh",50000,"cse")
aa.display()