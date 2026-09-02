# Create an abstract class Account with balance and abstract method calculate_interest(). Create SavingsAccount and CurrentAccount.
from abc import ABC,abstractmethod
class Account(ABC):
    def __init__(self,balance):
        self.balance=balance
    @abstractmethod
    def calculate_interest(self):
         pass
class SavingAccount(Account):
    def calculate_interest(self):
        interest=self.balance*10/100
        print("SavingAccount",interest)

class CurrentAccount(Account):
    def calculate_interest(self):
        interest=self.balance*12/100
        print("currentAccount",interest)

aa=SavingAccount(10000)
aa.calculate_interest()
ab=CurrentAccount(20000)
ab.calculate_interest()

