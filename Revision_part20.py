
# inheritance
class parent:
    def h(self):
        print("this is parent class")
class child(parent):
    def a(self):
        print("this is child class")
obj=child()
obj.h()
obj.a()

# parametrized constructor
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

# non_parametried constructor.
class student:
    def __init__(self):
        print("hello")
s1=student()

# super function()
class parent:
    def show(self):
        print("parent classs")
class child(parent):
    def display(self):
        super().show()
        print("child class")
obj=child()
obj.display()

# single interitance
class parent:
    def show(self):
        print("this is parent class")
class child(parent):
    pass
obj=child()
obj.show()

# mutiple interitance
class parent1:
    def show(self):
        print("first parent")
class parent2:
    def display(self):
        print("second parent")
class child(parent1,parent2):
    pass
obj=child()
obj.show()
obj.display()

# multilevel interitance
class parent:
    def show(self):
        print("this is grandfather")

class child1(parent):
    def dispaly(self):
     print("this is a father")

class child2(child1,parent):
   pass 
obj=child2()
obj.show()
obj.dispaly()