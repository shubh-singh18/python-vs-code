
# 1. Bank Account System — Encapsulation

# Create a BankAccount class with:
# - account_number
# - account_holder
# - balance

# Requirements:
# - Balance should not be directly accessible from outside the class.
# - Create deposit(amount) and withdraw(amount) methods.
# - Do not allow withdrawal if the balance is insufficient.
# - Create a get_balance() method to check the current balance.

class BankAccount:
    def __init__(self,account_number,account_holder,balance):
        self.__account_number=account_number
        self.__account_holder=account_holder

        self.__balance=balance
        print("balance",self.__balance)

    def deposit(self,amount):
        self.__balance+=amount
        print("deposite",amount)

    def withdrawal(self,amount):
        if self.__balance>=amount:
         self.__balance-=amount
         print("withdrawal",amount)
        else:
           print("invalid balance")

    def get_balance(self):
       print("total_balance",self.__balance)

aa=BankAccount(1234,"shubh",3000)
aa.deposit(500)
aa.withdrawal(200)
aa.get_balance() 






    
