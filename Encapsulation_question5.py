# Create a BankAccount class with private __balance. Create deposit() and withdraw() methods.
#  Withdrawal should happen only if sufficient balance is available.
class BankAccount:
    def __init__(self):
        self.__balance=0

    def deposit(self,amount):
        self.__balance+=amount

    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount
            print("withdraw successfully")
            print("reamining balance",self.__balance)
        else:
            print("Insufficient balance")

aa=BankAccount()
aa.deposit(2000)
aa.withdraw(400)


       
