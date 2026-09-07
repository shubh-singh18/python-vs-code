class a:
    def add(self,a,b):
        self.a=a
        self.b=b
        print(a+b)
class b:
    def sub(self,a,b):
        self.a=a
        self.b=b
        print(a-b)

class ss(a,b):
    def mul(self,a,b):
        self.a=a
        self.b=b
        print(a*b)
class pp(ss):
    def div(self,a,b):
        self.a=a
        self.b=b
        print(a/b)
ccc=pp()
ccc.add(10,20)
ccc.sub(40,30)
ccc.mul(5,10)
ccc.div(100,5)


    
      
       



