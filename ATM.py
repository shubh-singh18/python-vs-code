# class ATM:
#     def __init__(self):
#         self.pin=''
#         self.balance=0
#         self.menu()

#     def menu(self):
#         user_input=input("""
#         Hi How can I help you?
#         1.Press 1 to create Pin
#         2.Press 2 to change pin
#         3.Press 3 to check_balance
#         4.Press 4 to withdraw
#         Anything else to exit
#         """)
#         if user_input=='1':
#             #create pin
#             self.create_pin()
        
#         elif user_input=='2':
#             #change pin
#             self.change_pin()
#         elif user_input=='3':
#             #check_balance
#             self.check_balance()
#         elif user_input=='4':
#             #withdraw
#             self.withdraw()
#         else:
#             exit()
#             self.menu()

#     def create_pin(self):
#         user_pin=input("enter a pin")
#         self.pin=user_pin

#         user_balance=int(input("enter a balance"))
#         self.balance=user_balance
#         print("create pin successfully")
#         self.menu()

#     def change_pin(self):
#           old_pin =input('enter old pin')
   
#           if old_pin ==self.pin:
#              #let him change the pin
#              new_pin =input('entert new pin')
#              self.pin =new_pin
#              print('pin change successfull')
#              self.menu()
#           else:
#              print('nai karne de sakta re baba')
#              self.menu()

#     def check_balance(self):
#         user_pin=input("enter a pin")
#         if self.pin==user_pin:
#             print("your balance is",self.balance)
#             self.menu()
#         else:
#             print("wrong pin enter ")
#             self.menu()

#     def withdraw(self):
#         user_pin=input("enter a pin")
#         if user_pin==self.pin:
#             amount=int(input("enter a amount"))
#             if amount<=self.balance:
#                 self.balance=self.balance-amount
#                 print("withdraw is successfully",self.balance)
#             else:
#                 print("bsdk garib")
            
#         else:
#             print("enter a right pin")
#             self.menu()


# obj=ATM()

class fraction:
    def __init__(self,x,y):
        self.num=x
        self.den=y

    def __str__(self):
        return '{}/{}'.format(self.num,self.den)

    def __add__(self,other):
        new_num=self.num*other.den + other.num*self.den
        new_den=self.den*other.den
        return '{}/{}'.format(new_num,new_den)

    def __sub__(self,other):
        new_num=self.num*other.den - self.den*other.num
        new_den=self.den*other.den
        return '{}/{}'.format(new_num,new_den)

    def __mul__(self,other):
        new_num=self.num*other.num 
        new_den=self.den*other.den
        return '{}/{}'.format(new_num,new_den)

    def __truediv__(self,other):
        new_num=self.num*other.den
        new_den=self.den*self.num
        return '{}/{}'.format(new_num,new_den)


fr1=fraction(3,4)
fr2=fraction(1,2)
print(fr1)
print(fr1+fr2)
print(fr1-fr2)
print(fr1*fr2)
print(fr1/fr2)


        
        
