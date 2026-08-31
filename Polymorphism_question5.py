# Create a Calculator class with a multiply() method that can multiply 2, 3, or 4 numbers using default arguments.
class calculator:
    def multiple(self,a,b,c=1,d=1):
        return a*b*c*d
aa=calculator()
print(aa.multiple(10,5))
print(aa.multiple(10,5,2))
print(aa.multiple(10,5,2,2))












