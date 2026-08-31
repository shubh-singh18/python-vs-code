# Create a Product class with price and overload the + operator to calculate the total price of two products.
class Product:
    def __init__(self,price):
        self.price=price
    def __add__(self,other):
        return self.price+other.price
aa=Product(150)
ab=Product(400)
print(aa+ab)