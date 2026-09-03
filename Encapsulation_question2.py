# Create a BankAccount class with a private variable __balance. Create methods deposit() and display_balance().
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposite(self,amount):
        self.__balance+=amount

    def display_balance(self):
        print(self.__balance)


aa=BankAccount(5000)
aa.deposite(2000)
aa.display_balance()