class student:#class
    name="shiva"
s=student()#object
print(s.name)

class Rectangle:
    def __init__(self,x,y):
        self.len=x
        self.wid=y

    def Perimeter(self):
        return 2*(self.len*self.wid)

    def Area(self):
        return self.len*self.wid

    def display(self):
        print(self.len)
        print(self.wid)
        print(self.Perimeter())
        print(self.Area())

aa=Rectangle(3,4)
aa.display()