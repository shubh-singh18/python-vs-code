# Create a Mobile class with private __price. Create methods to set and get the price.
class Mobile:
    def __init__(self):
        self.__price=0

    def set_price(self,price):
        self.__price=price

    def get_price(self):
        print(self.__price)

aa=Mobile()
aa.set_price(350)
aa.get_price()