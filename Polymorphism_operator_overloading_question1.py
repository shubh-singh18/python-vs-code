# Create a Distance class and overload the + operator to add two distance objects.
class Distance:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.a
aa=Distance(20)
ab=Distance(40)
print(aa+ab)