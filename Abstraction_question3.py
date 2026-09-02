# Create an abstract class Shape with an abstract method area(). Create Rectangle class to calculate area.
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print(self.length*self.width)

aa=Rectangle(7,8)
aa.area()