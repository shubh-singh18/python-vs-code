# Create a Product class with a price() method. Create an Electronics class that overrides price() and displays
#  the product price after discount.
class Product:
    def Price(self):
        print("Product price")
class Electronics(Product):
    def Price(self):
        price=50000
        discount=10
        final_price=price-(price*discount/100)
        print("final-price",final_price)

aa=Electronics()
aa.Price()


     
