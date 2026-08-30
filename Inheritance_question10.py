# create a bankaccount parent class with account_no and balance.create savingaccount and currentaccounnt child classes.use inheritance 
# to perform deposite and withdrawal operations.
class Bank_Account:
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance

    def deposite(self,amount):
        self.balance +=amount
        print("amount deposite",amount)
        print("current balance",self.balance)

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("amount withdraw",amount)
            print("current balance",self.balance)
        else:
            print("Insufficient balance")

class Savingaccount(Bank_Account):
    def saving_acc(self):
        print("this is saving account")

class Currentaccount(Bank_Account):
    def current_acc(self):
     print("this is current account")

#saving account
s1=Savingaccount(101,10000)
s1.saving_acc()
print("Account no",s1.account_no)
s1.deposite(2000)
s1.withdraw(1000)
print()

#current Account
c1=Currentaccount(102,20000)
c1.current_acc()
print("Account no",c1.account_no)
c1.deposite(4000)
c1.withdraw(3000)
