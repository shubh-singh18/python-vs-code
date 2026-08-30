# Create an Employee class with name,salary,and department.create an object and display all details.
class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def display(self):
        print(self.name,self.salary,self.department)
aa=Employee("devansh",35000,"cse")
aa.display()
