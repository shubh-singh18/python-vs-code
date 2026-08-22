# Create a Vehicl-e class. Create Car and Bike classes that inherit from Vehicle

class Vehicle:
    def __init__(self,color):
        self.color=color

class car(Vehicle):
    def c(self):
       
        print(f"this is a {self.color} car")
class bike(Vehicle):
    def b(self):
       
        print(f"this is a {self.color} bike")
aa=car("black")
aa.c()
ab=bike("red")
ab.b()


