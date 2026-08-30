#Create a student class with name and age.create  an object and display the details.
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
aa=student("shivam",20)
aa.display()

