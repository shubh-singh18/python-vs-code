# Create an Account class with a withdraw() method. Create a SavingAccount class that overrides withdraw() with its own withdrawal logic.
class Account:
    def withdraw(self):
        pass
class SavingAccount(Account):
    def withdraw(self):
        print("withdraw done")
aa=SavingAccount()
aa.withdraw()