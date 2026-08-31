# Create a Shape class with an area() method that calculates the area of:

# square
# rectangle
# using default arguments.

class shape:
    def area(self,length=7,breadth=None):
        if breadth is None:
            print("area of square",length*length)
        else:
            print("area of rectangle",length*breadth)
aa=shape()
aa.area()
aa.area(10,5)


