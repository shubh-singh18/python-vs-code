# class student:
#      branch="cse"
#      name="shubh"
#      age="20"
#      @classmethod
#      def ab(cls):

#          print(cls.branch,cls.name,cls.age)
# student.ab()



# class s:
#     def __init__(self,name):
#         self.name=name
#     @classmethod
#     def cc(cls):
#         cls.name="shivam"
#         print(cls.name)
# a=s("aman")
# s.cc()

# class s:
#     def __init__(self,name):
#         self.name=name
#     @classmethod
#     def cc(cls):
#         cls.name="sh8u7iva"
#         print(cls.name)
# a=s("aman")
# s.cc()

class ATM:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()

    def menu(self):
        user_input =input("""
        Hi How can I help you
        1. Press 1 to create  pin
        2. Press 2 to change pin 
        3. Press 3 to check_balance
        4. Press 4 to withdraw
        5.Anything else to exit
""")

        if user_input=='1':
            self.create_pin()

        elif user_input=='2':
            self.change_pin()

        elif user_input=='3':
            self.check_balance()

        elif user_input=='4':
            self.withdraw()

        else:
            exit()

    def create_pin(self):
      user_pin=input('enter a pin')
      self.pin=user_pin
      user_balance=input('enter a balance')
      self.balance=user_balance
      print("pin created successfully")
      self.menu()

    def change_pin(self):
        old_pin=input("enter a old pin")
        if old_pin==self.pin:
         new_pin=input('enter a new pin')
         self.pin=new_pin
         print('pin change successfully')
         self.menu
        else:
            print("wrong password")
            self.menu

    def check_balance(self):
        user_pin=input("enter your pin")
        if self.pin==user_pin:
            print("your balance is",self.balance)
            self.menu
        else:
            print("wrong pin")
            self.menu()

    def withdraw(self):
        user_pin=input("enter the pin")
        if user_pin==self.pin:
            amount=int(input("enter a amount"))
            if amount<=self.balance:
              self.balane=self.balace-amount
              print('withdrawal successfully.balance is',self.balance)
            else:
              print('bskd ke garib')
        else:
            print('wrong pin')
        self.menu

obj=ATM()


        

