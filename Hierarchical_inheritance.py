#Hierarchical_inheritance
class Parent:
    def parent(self):
        print("I am parent")

class Child1(Parent):
    def child1(self):
        print("I am first child")

class Child2(Parent):
    def child2(self):
        print("I am second child")

aa=Child1()
aa.parent()
aa.child1()
ab=Child2()
ab.parent()
ab.child2()
