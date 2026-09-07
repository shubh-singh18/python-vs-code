class a:
    def add(self):
        a=20
        b=30
        print(a+b)
class child1(a):
    def sub(self):
        a=30
        b=12
        print(a-b)
        super().add()
class child2(a):
    def div(self):
        a=50
        b=5
        print(a/b)
        super().add()
aa=child1()
a1=child2()
aa.sub()
a1.div()
