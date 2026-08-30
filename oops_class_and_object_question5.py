#create a bankaccount class with account_no and balance.create an object and dispaly the account details
class BankAccount:
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance
    def display(self):
        print(self.account_no,self.balance)
aa=BankAccount(12345,30000)
aa.display()