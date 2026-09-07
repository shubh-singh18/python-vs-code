class ATM:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()

    def menu(self):
        user_input=input("""
        Hi How can I help you?
        1.Press 1 to create pin
        2.Press 2 to change pin
        3.Press 3 to check balance
        4.Press 4 to withdraw
        5.Anything else to exit
        """)
        if user_input =='1':
            #create pin
            self.create_pin()
            
        elif user_input=='2':
            #change pin
            self.change_pin()
        elif user_input=='3':
            #check balance
            self.check_balance()
        elif user_input=='4':
            #withdraw
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin=input("enter a pin")
        self.pin = user_pin

        user_balance=int(input("enter a balance"))
        self.balance=user_balance
        print("pin created successfully")
        self.menu()

    def change_pin(self):
        old_pin=input("enter old pin")
        if old_pin==self.pin:
            new_pin=input("enter a new pin")
            self.pin=new_pin
            print("pin change successfully")
            self.menu()

        else:
            print("not change your wrong pin enter")
            self.menu()

    def check_balance(self):
        user_pin=input("enter your pin")
        if user_pin==self.pin:
            print("Your balance",self.balance)
            self.menu()
        else:
            print("wrong pin enter your")
            self.menu()
        

    def withdraw(self):
        user_pin=input("enter the pin")
        if user_pin==self.pin:
            amount=int(input("enter a amount"))
            if amount<=self.balance:
               self.balance = self.balance-amount
               print("withdrawl successfully.balance is",self.balance)
            else:
              print("bsdk garib")
        else:
            print("sala chor")
            
            
obj=ATM()