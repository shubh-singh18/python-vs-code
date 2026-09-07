# class a:
#     def dog(self):
#         print("Kutta bhauk raha hai")
# class b(a):
#     def cat(self):
#         print("cat is muing")

# ob=b()
# ob.dog()
# ob.cat()

class a:
    def add(self):
        a=10
        b=20
        print(a+b)

    def sub(self):
        a=20
        b=15
        print(a-b)

class b(a):
    def mul(self):
        a=5
        b=5
        print(a*b)

    def div(self):
        a=100
        b=5
        print(a/b)

ab=b()
ab.add()
ab.sub()
ab.mul()
ab.div()

class a:
    def __init__(self):
      print("hello")
x=a()
        
class a:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
        print(name,branch)
ab=a("shivam","cse")

#parents class ko hmm super class bolate hai
class add:
    def a(self):
        print("this is parent class method")
class b(add):
    def b(self):
        print("this is chlid method")
        super.a()
obj=b()
obj.a()
obj.a()




