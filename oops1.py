# class s:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name,self.age,"this is prasent")
# class a(s):
#     def show(self):
#         print("this is child")
# ab=s("shubh",19)
# ab.display()
# print(ab.age)
#mutilevel

# class a:
#     def m(self):
#         print("hello")

# class aa(a):
#     def k(self):
#         print("this hello")
# class ab(aa):
#     pass
# mm=ab()
# mm.m()
# mm.k()

class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age,"this is parent")
class teacher(student):
    def __init__(self,rollno):
        self.roll.no=rollno

    def show(self):
        print(self.rollno,"this is child")
class principle(teacher):
    pass
ab=student("shubh",23)
ab.display()



