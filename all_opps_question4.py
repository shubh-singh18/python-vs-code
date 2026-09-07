# 4. Shape Area Calculator — Abstraction + Polymorphism

# Create an abstract class Shape with an abstract method area().

# Create:
# - Circle
# - Rectangle
# - Triangle

# Requirements:
# - Each class must implement area().
# - Create objects of all three classes.
# - Store them in a list.
# - Use a loop to calculate the area of every shape.

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print("circle of area",3.14*self.radius*self.radius)

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print("Rectangle of area",self.length*self.width)

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        print("Triangle of area",0.5*self.base*self.height)

aa=Circle(5)
ab=Rectangle(10,6)
ac=Triangle(12,8)
list=[aa,ab,ac]
for i in list:
    (i.area())
                   






    




























    



