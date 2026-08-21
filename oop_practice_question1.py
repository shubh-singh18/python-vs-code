# Create a Person class with name and age. Create a Student class that inherits from Person and adds roll_no and course.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class student(Person):
    def __init__(self,name,age,rollno,course):
        super().__init__(name,age)
        self.rollno=rollno
        self.course=course
    def display(self):
        print("name",self.name)
        print("age",self.age)
        print("rollno",self.rollno)
        print("course",self.course)

aa=student("shubh",20,10008,"btech")
aa.display()
      

