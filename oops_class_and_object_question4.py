#create a rectangle class with length and width .create an object and calculate its area.
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def display(self):
        print(self.length*self.width)
aa=Rectangle(4,6)
aa.display()