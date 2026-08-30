#create a Person class with name and age. creates a student class that inherits from person and adds roll_no.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class student(Person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no=roll_no

    def display(self):
        print(self.name,self.age,self.roll_no)
aa=student("shivam",23,1001)
aa.display()