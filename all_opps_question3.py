# 3. Vehicle Rental System — Inheritance + Polymorphism

# Create a Vehicle class with:
# - brand
# - model
# - rental_price

# Create three child classes:
# - Car
# - Bike
# - Truck

# Requirements:
# - Create a calculate_rent(days) method.
# - Each vehicle type should calculate rent differently.
# - Use method overriding.

class vechile:
    def __init__(self,Brand,Model,Rental_price):
        self.Brand=Brand
        self.Model=Model
        self.Rental_price=Rental_price

    def calculate_rent(self,days):
        pass

class Car(vechile):
    def calculate_rent(self, days):
        total=self.Rental_price*days+500
        print("car is vechile",total)

class Bike(vechile):
    def calculate_rent(self, days):
        total=self.Rental_price*days+200
        print("bike is vechile",total)

class truck(vechile):
    def calculate_rent(self, days):
        total=self.Rental_price*days+800
        print("Truck is vechile",total)

aa=Car("TATA","Newmobel",10000)
aa.calculate_rent(3)

ab=Bike("Bullet","Royal_Enfield",8000)
ab.calculate_rent(5)

ac=truck("Tata","newmobel",12000)
ac.calculate_rent(2)
