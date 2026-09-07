# class parent:

#     def c(self):
#         print("this is parent class method")

# class child(parent):
#     def c(self):
#         super().c()
#         print("this is child class method")
       
# obj=child()
# obj.c()  
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def dispaly(self):
        print(f"name{self.name},marks{self.marks}")
ab=student("shubh",98)
ab.dispaly()


class ab:
    def __init__(self):
        print("hello i am constructor")
obj=ab();

class ab:
    def __init(self,name,branch):
        self.name=name
        self.branch=branch
        print(self.name,self.branch,'this is parsent')
    
class bb(ab):
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
        print(self.name,self.branch,"this is child")
        super().__init__("shubh","cse")
       
c=bb("sun","cse")

#type of inherticance
#single inherticance
class a:
    def cc():
        print("this is child")
class b(a):
    pass
oo=b()
b.cc()

#multiple inhertance
class a:
    def cc(self):
        print("thsi is child")
class d:
    def pp(self):
        print("this is the method of d class")
class b(a,d):
    pass
oo=b()
oo.cc()
oo.pp()

#mutiple level inhertance
class a:
    def cc(self):
        print("this is child")
class d(a):
    def pp(self):
        print("this is the method of d class")
class b(d):
    pass
oo=b()
oo.cc()
oo.pp()

#single Inheritance
# A child class inherits from only one parent class

class a:
    def cc():
        print("this is child")
class b(a):
    pass
oo=b()
b.cc()

# Mutiple Inheritance
# A child class inherits directly from more than one parent class.

class a:
    def cc(self):
        print("this is child")
class d:
    def pp(self):
        print("this is the method of d class")
class b(a,d):
    pass
oo=b()
oo.cc()
oo.pp()

# Multilevel Inheritance
# A chain of inheritance where a derived class inherits from another derived class. 
class a:
    def cc(self):
        print("this is child")
class d(a):
    def pp(self):
        print("this is the method of d class")
class b(d):
    pass
oo=b()
oo.cc()
oo.pp()


