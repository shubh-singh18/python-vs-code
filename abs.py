from abc import ABC,abstractmethod
class a(ABC):
    @abstractmethod
    def add(self):
        pass
class b(a):
    @abstractmethod
    def sub(self):
        pass
class c(b):
    @abstractmethod
    def mul(self):
        pass
class cc(c):
    def add(self):
        a=10
        b=20
        print(a+b)
    def sub(self):
            a=10
            b=20
            print(a-b)
    def mul(self):
            a=10
            b=20
            print(a*b)
obj=cc()
obj.add()
obj.sub()
obj.mul()

class a:
     def add(self,a,b):
          print(a+b)
     def add(self,a,b):
          print(a-b)
obj=a()
obj.add(200,100)