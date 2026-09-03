# Create a BankAccount class with private __balance and methods:

# deposit()
# withdraw()
# get_balance()

# Apply proper validation for deposit and withdrawal.

class BankAccount:
    def __init__(self):
        self.__balance=0

    def deposit(self,amount):
        if amount>=0:
            self.__balance=amount
            print("deposit",self.__balance)
        else:
            print("invalid balance")

    def withdraw(self,amount):
        if amount>=0 and amount<=self.__balance:
            self.__balance-=amount
            print("withdraw",self.__balance)
        else:
            print("invalid balance")

    def get_balance(self):
        print(self.__balance)
aa=BankAccount()
aa.deposit(2000)
aa.withdraw(300)
aa.get_balance()