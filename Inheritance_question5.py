#create Employee as a parent class and developer as a child class.Display employee name,salary,and programming language.
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class developer(Employee):
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language

        
    def display(self):
        print("name",self.name)
        print("salary",self.salary)
        print("programming_language",self.programming_language)
aa=developer("devansh",40000,"python")
aa.display()




