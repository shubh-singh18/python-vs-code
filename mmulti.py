class parent:
    def s(self):
        print("hello this is parent")

class child1(parent):
    pass
class child2(parent):
    pass
ss=child1()
s2=child2()
ss.s()
s2.s()
