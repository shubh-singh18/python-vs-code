# Create a Box class with length and width. Overload the == operator to check whether two boxes have the same dimensions.
class Box:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def __eq__(self,other):
        return self.length==other.length and self.width==other.width

aa=Box(60,80)
ab=Box(60,80)
print(aa==ab)