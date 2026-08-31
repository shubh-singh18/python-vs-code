#create a calculator class with a method add() that can add 2 or 3 numbers using default arguments:
class calculator:
    def add(self,a,b,c=0):
        return a+b+c
aa=calculator()
print(aa.add(50,60))
print(aa.add(100,200,300))
