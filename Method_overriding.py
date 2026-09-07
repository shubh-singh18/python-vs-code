# class a:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b):
#         print(a-b)
# obj=a()
# obj.add(200,100)

class Bank:
    def amount(self,balance):
        self.balance=balance
        print(self.balance)
    def intrest(self,rate):
        self.rate=rate
        print(self.rate)
        rate=(self.balance*self.rate*self.Time)/100
    def Time(self,time):
        self.time=time
        print(self.time)

class General(Bank):
    def h(self):
        G=((self.balance*self.rate*self.time)/100)
        print(G)
        print(G-(G*(10/100)))

class obc(Bank):
    def j(self):
        G=((self.balance*self.rate*self.time)/100)
        print(G)
        print(G-(G*(20/100)))

class st(Bank):
    def k(self):
        G=((self.balance*self.rate*self.time)/100)
        print(G)
        print(G-(G*(30/100)))

g=General()
ob=obc()
sc=st()
g.amount(5000000)
g.intrest(10)
g.time(2)
g.h()
g.j()
g.k()


class bank:
    def a(self,principal=500000,rate=10,time=2):
        self.principal=500000
        self.rate=10
        self.time=2
        intrest=(self.principal*self.rate*self.time)/100
        print(intrest)
class general(bank):
    def g(self):
        h= intrest=(self.principal*self.rate*self.time)/100
        print(h-(h*(10/100)))
class obc(bank):
    def O(self):
        h= intrest=(self.principal*self.rate*self.time)/100
        print(h-(h*(20/100)))
class stsc(bank):
    def S(self):
        h= intrest=(self.principal*self.rate*self.time)/100
        print(h-(h*(30/100)))

b=stsc()
b.S()
J=general()
J.g()
i=obc()
i.O()





      



    


