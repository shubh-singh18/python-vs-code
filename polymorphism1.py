
# create a vehicle class with start() method. create car and bike classes that provide thier own  implementation.
class Vehicle:
    def start(self):
        print("vihicle start")
class car(Vehicle):
    def start(self):
        print("car start key")
class Bike(Vehicle):
    def start(self):
        print("Bike start self-key")
Bike=Bike()
car=car()
Bike.start()
car.start()



#create animal class with sound()method.create dog,cat,and cow.
class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        print("Dog says:bark")
class Cat(Animal):
    def sound(self):
        print("cat says:meow")
class cow(Animal):
    def sound(self):
        print("cow says:moo")
Dog=Dog()
Cat=Cat()
cow=cow()
Dog.sound()
Cat.sound()
cow.sound()


    
# create a shape class with a area() method.create circle and rectangle classes that override area().
class Shape:
    def area(self):
        print("shape of area")

class Circle:
    def Circle(self):
        radius=5
        print(3.14*radius*radius)

class Rectangle:
    def Rectangle(self):
        length=10
        breath=5
        print(length*breath)
aa=Circle()
ab=Rectangle()
aa.Circle()
ab.Rectangle()


#dunder method
#ye program dunder method se hmm add kar rhe hai two number ka.
class a:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self, other):
        return self.marks+other.marks
aa=a(50)
ab=a(40)
print(aa+ab)


# three or more number ko add kar ne ke liye ye method haI

class b:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self, other):
        return b(self.marks+other.marks)
aa=b(50)
ab=b(60)
ac=b(100)
ad=b(200)
res=aa+ab+ac+ad
print(res.marks)
 

#without dunder operator overloading perform nhi karte hai
#Example

class a:
    def __init__(self,marks):
        self.marks=marks
aa=a(50)
ab=a(40)
print(aa+ab)






