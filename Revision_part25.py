
# generator
def a():
    yield 1
    yield 3
x=a()
print(next(x))
print(next(x))

# decorator in python
def decorator(func):
    def wrapper():
        print("befor")
        func()
        print("after")
    return wrapper
@decorator
def hello():
    print("hello")
hello()




# class
class student:#class
    name="shubhsingh"
#object
s1=student()#object
print(s1.name)

# __init__
class student:
    def __init__(self,name):
        self.name=name
s1=student("shubh")
print(s1.name)

# class attributes
class student:
    name="shubhsingh"

# instance attributes
class student:
    def __init__(self,name):
        self.name=name

# instance method.
class student:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
s1=student("singh")
s1.show()

# class method
class student:
    branch="cse"
    @classmethod
    def show(cls):
        print(cls.branch)
student.show()

# inheritance in python
class parent:
    def display(self):
        print("this is a parent class")
class child(parent):
    def show(self):
        print("this is a child class")
s1=child()
s1.display()
s1.show()


# parameterized constructor
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

# non_parameterized construct
class student:
    def display(self):
        print("hello")
s1=student()
s1.display()


