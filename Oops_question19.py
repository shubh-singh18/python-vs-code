# 19. Create a Parking Payment System using Strategy Pattern.
#     Implement different payment methods such as Cash, Card, and UPI.
#     The system should allow changing the payment strategy dynamically

class Payment:
    def pay(self):
        pass

class Cash(Payment):
    def pay(self,amount):
        print(amount)

class Card(Payment):
    def pay(self,amount):
        print(amount)

class UPI(Payment):
    def pay(self,amount):
        print(amount)

class Parking_Payment:
       def __init__(self,payment):
           self.payment=payment

       def make_payment(self,amount):
           self.payment.pay(amount)

       def change_payment(self,payment):
           self.payment=payment

ab=Parking_Payment(Cash())
ab.make_payment(100)

ab.change_payment(Card())
ab.make_payment(200)

ab.change_payment(UPI())
ab.make_payment(300)        


