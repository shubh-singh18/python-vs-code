#multi-level_inheritance
class Grandfather:
    def grandfather(self):
        print("I am grandfather")

class Father(Grandfather):
    def Father(self):
        print("I am Father")

class Child(Father):
    def Child(self):
        print("I am child")

aa=Child()
aa.grandfather()
aa.Father()
aa.Child()