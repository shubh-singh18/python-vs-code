# 7. Payment System — Abstraction + Polymorphism

# Create an abstract class Payment with an abstract method:

# pay(amount)

# Create:
# - CreditCardPayment
# - UPIPayment
# - CashPayment

# Requirements:
# - Each class should implement pay() differently.
# - Create one common function that accepts any Payment object.
# - Use polymorphism to process all payment types


from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class creditcard(Payment):
    def pay(self,amount):
        print("payment paid by creaditcard",amount)
class UPI(Payment):
    def pay(self,amount):
        print("payment paid by upi",amount)
class cash(Payment):
    def pay(self,amount):
     print("payment paid by cash",amount)
def pro(payment,amount):
    payment.pay(amount)
cc=creditcard()
up=UPI()
ca=cash()
pro(cc,100)
pro(up,100)
pro(ca,100)
