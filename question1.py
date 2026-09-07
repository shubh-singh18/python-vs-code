# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.

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





