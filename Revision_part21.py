
# Hierarchical Inheritance
class parent:
    def show(self):
        print("this is parent class")
class child1(parent):
    pass
class child2(parent):
    pass
o=child1()
o=child2()
o.show()

# hybrid inheritance 
class parent:
    def show(self):
        print("this is parent class")
class child1(parent):
    def display(self):
        print("this is child1 class")
class child2(parent):
    def he(self):
        print("this is child2 class")
class son(child1,child2):
    pass
obj=son()
obj.show()
obj.display()
obj.he()

# # python cannot support method overloading
# class parent:
#     def show(a,b):
#         print(a+b)
#     def show(a,b,c):
# obj=parent()
# obj.show(10,20,30)

# default arguments
class parent:
    def add(self,*args):
        print(sum(args))
obj=parent()
obj.add(10,20)
obj.add(10,20,30)