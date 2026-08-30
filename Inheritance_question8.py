#create a vehicle parent class and car,bike and bus child classses.Add diffferent methods to each child.
class Vehicle:
    def __init__(self,brand):
        self.brand=brand
class Car(Vehicle):
    def __init__(self,color,brand):
        super().__init__(brand)
        self.color=color
    def display1(self):
        print(self.brand)
        print(self.color)
class Bike(Vehicle):
    def __init__(self,color,brand):
        super().__init__(brand)
        self.color=color
    def display2(self):
        print(self.brand)
        print(self.color)
class Bus(Vehicle):
    def __init__(self,color,brand):
        super().__init__(brand)
        self.color=color
    def display3(self):
        print(self.brand)
        print(self.color)
aa=Car("blue","honda")
ab=Bike("red","yamaha")
ac=Bus("yellow","tata")
aa.display1() 
ab.display2()
ac.display3()                                                        