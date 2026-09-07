#example
#parent class
class user:
    def __init__(self):
        self.name ="nitish"

    def login(self):
        print("login")

#child class
class student(user):
    def enroll(self):
        print("enroll into the course")

u=user()
s=student()
print(s.name)
s.login()
s.enroll()

#child can't access private members of the class
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand=brand
        self.camera=camera

    def show(self):
        print(self.__price)

class smartPhone(Phone):
    def check(self):
        print(self.__price)

s=smartPhone(45000,"apple",14)
print(s.brand)
s.show()

#method overriding
class phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price =price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Buying a phone")

class smartphone(phone):
    def buy(self):
        print("Buying a smartphone")

s=smartphone(200000,"appple",18)
s.buy()


#super keyword
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")
        # syntax to call parent ka buy method
        super().buy()

s=SmartPhone(200000,"Apple",18)
s.buy()

#single inheritance
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price =price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("buying a phone")

class SmartPhone(Phone):
    pass
a=SmartPhone(20000,"apple","17pro")
a.buy()
print(a.brand)

# Multilevel
class Product:
    def review(self):
        print("Product customer review")
        
class Phone(Product):
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    pass
s=SmartPhone(20000,"Apple",19)
s.buy()
s.review()
