# Create an abstract class Payment with an abstract method pay(). Create UPI and CardPayment classes and implement pay() differently.
from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment):
    def pay(self):
        print("pay the upi")
class CardPayment(Payment):
    def pay(self):
        print("pay the cardpayment")

aa=UPI()
aa.pay()
ab=CardPayment()
ab.pay()