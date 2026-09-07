# : Bank Account and Savings Account
# Create a class BankAccount with accountHolder and balance.
# Create a class SavingsAccount that inherits from BankAccount and adds interestRate.
# Calculate the interest and final balance.
# Formula:
# Interest = Balance × Interest Rate / 100
# Example:
# Balance = 10000
# Interest Rate = 5

# Interest = 500
# Final Balance = 1050

class BankAccount:
    def __init__(self,acc,bal):
        self.acc=acc
        self.bal=bal

class savingaccount(BankAccount):
    def __init__(self,acc,bal,inte):
        super().__init__(acc,bal)
        self.inte=inte

    def cc(self):
        inte=self.bal * self.inte/100
        finalbal=self.bal+inte
        print("account holder=",self.acc)
        print("bal=",self.bal)
        print("inte=",inte)
        print("final balance",finalbal)
aa=savingaccount("shiva",2000,10)
aa.cc()
