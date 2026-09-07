
# 6. E-Commerce Product System — Inheritance + Polymorphism

# Create a Product class with:
# - name
# - price
# - stock

# Create child classes:
# - Electronics
# - Clothing
# - Grocery

# Requirements:
# - Create a get_discount() method.
# - Override it in every child class.
# - Each product type should have a different discount.
# - Calculate the final price after discount.

class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
class Electronics(Product):
    def Get_disscount(self):
        discount=self.price-(self.price*12/100)
        print("Electronics Discount",discount)
        total=self.price-discount

        print(self.name)
        print(self.stock)
        print(self.price)
        print(total)
class clothing(Product):
    def Get_disscount(self):
        discount=self.price-(self.price*15/100)
        print("clothing Discount",discount)
        total=self.price-discount

        print(self.name)
        print(self.stock)
        print(self.price)
        print(total)
class grocery(Product):
    def Get_disscount(self):
        discount=self.price-(self.price*18/100)
        print("grocery Discount",discount)
        total=self.price-discount

        print(self.name)
        print(self.stock)
        print(self.price)
        print(total)
()
obj=Electronics("shubh",10000,2)
obj.Get_disscount()
ob=clothing("Devansh",1000,5)
ob.Get_disscount()
O=grocery("shivam",200000,1)
O.Get_disscount()