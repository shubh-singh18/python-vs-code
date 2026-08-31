# 6. Create a Calculator class with add() and subtract() methods that work with different numbers of arguments.
class calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
    def sub(self,a,b=0,c=0):
        return a-b-c
aa=calculator()
print(aa.add(10))
print(aa.add(10,20))
print(aa.add(10,20,30))

print(aa.sub(100))
print(aa.sub(100,50))
print(aa.sub(100,50,30))