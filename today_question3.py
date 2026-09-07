# Create a parent class named Person with name and age. Create a child class named Student that 
# inherits Person and adds roll number and course. Create an object and display all details.
class Person:
     def __init__(self,name,age):
          self.name=name
          self.age=age
     def show(self):
          print(self.name,self.age)
     
class Student(Person):
     def __init__(self,roll_no,course,name,age):
          self.roll_no=roll_no
          self.course=course
          self.name=name
          self.age=age
          super().__init__(self.name,self.age)

     def aa(self):
              print(self.roll_no,self.course)

a=Student("shubh",20,1001,"cse")
a.aa()
a.show()




   
