# Create a Shape class with an area() method. Create a Circle class that overrides area() to calculate the area of a circle.
class Shape:
    def area(self):
        print("this is shape")
      
class Circle(Shape):
    def area(self,radius):
        area=3.14*radius*radius
        print("area of circle",area)
aa=Circle()
aa.area(7)
