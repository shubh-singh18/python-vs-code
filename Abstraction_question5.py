# Create an abstract class Bank with methods deposit() and withdraw(). Create SBI class and implement both methods.
from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class SBI(Bank):
    def deposit(self):
        print("the amount deposite is 4000")
    def withdraw(self):
        print("the withdraw amount is 2000")

aa=SBI()
aa.deposit()
aa.withdraw()