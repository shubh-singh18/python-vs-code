#Multiple_inheritance
class Parent1:
    def parent1(self):
        print("I am father")

class Parent2:
    def parent2(self):
        print("I am mother")

class Child(Parent1,Parent2):
    def child(self):
        print("I am child")
aa=Child()
aa.parent1()
aa.parent2()
aa.child()