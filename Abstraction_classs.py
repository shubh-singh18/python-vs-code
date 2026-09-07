class Student:
    def __init__(self,name,age,branch):
        self.name=name
        self.age=age
        self.branch=branch

    def display(self):
        print(self.name,self.age,self.branch)

aa=Student("shubh",19,"cse")
aa.display()
