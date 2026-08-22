# Create two classes Father and Mother. Create a Child class that inherits from both and access methods from both classes.

class Father:
    def f(self):
        print("this is a father")
class Mother():
    def m(self):
        print("this is a mother")
class son(Mother,Father):
    def s(self):
        print("this is a son")
aa=son()
aa.f()
aa.m()
aa.s()


