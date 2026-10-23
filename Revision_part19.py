
# oops
# class 
class student:
    name="shubh"
    age=21
# object
s1=student()
print(s1.name)
print(s1.age)

# __init__ method
# class
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
# object
s1=student("shubh",20)
print(s1.name)
print(s1.age)


# class attributes
class student:
    name="shubh"

# instance attributes
class student:
    def __init__(self,name):
        self.name=name


# self -> ye cuurent object ko refers karta hai
# cls -> ye current class ko refers karta hai 


# instance mathod
class student:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
s1=student("shubh")
s1.show()

# class method..
class student:
    branch="cse"
    @classmethod
    def show(cls):
        print(cls.branch)
student.show()