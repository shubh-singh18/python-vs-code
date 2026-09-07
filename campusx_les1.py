# l=[1,2,3,4]
# print(type(l))

# l=[1,2,3,4]
# l.upper()

#banking application
class Atm:
    def __init__(self): #constructor
        self.pin=''
        self.balance=0
        self.menu()

    def menu(self):
       user_input =input("""
       Hi How can I help you?
       1. Press 1 to create pin
       2. Press 2 to change pin
       3. Press 3 to check balance
       4. Press 4 to withdraw
       5. Anything else to exit
       """)

       if user_input =='1':
        # create pin
        self.create_pin()
       elif user_input =='2':
        #change pin
        self.change_pin()
       elif user_input =='3':
           #check balance
           pass 
       elif user_input =='4':
           # withdraw
        self.withdraw()   
           
       else:
           exit()
           

    def create_pin(self):
        user_pin = input('enter your pin')
        self.pin = user_pin

        user_balance = int(input('enter balance'))
        self.balance = user_balance
        

        print('pin created successfully')
        self.menu()  

    def change_pin(self):
       old_pin =input('enter old pin')

       if old_pin ==self.pin:
          #let him change the pin
          new_pin =input('entert new pin')
          self.pin =new_pin
          print('pin change successfull')
          self.menu()
       else:
          print('nai karne de sakta re baba')
          self.menu()

    def check_balance(self):
     user_pin = input('enter your pin')
     if user_pin == self.pin:
        print('your balance is',self.balance)
     else:
        print("wrong pin")
        self.menu()
        
    def withdraw(self):
      user_pin = input('enter the pin')
      if user_pin == self.pin:
         amount =int(input('enter the amount'))
         if amount <=self.balance:
            self.balance =self.balance - amount
            print('withdrawl successful.balance is',self.balance)
           
         else:
            print('bskd garib')
      else:
         print('wrong pin')
      self.menu()
         
obj=Atm()


# create a first own datatype
class Fraction:
   #parameterized constructor
   def __init__(self,x,y):
      self.num = x
      self.den = y
   def __str__(self):
        return '{}/{}'.format(self.num,self.den)
   def __add__(self,other):
    new_num = self.num*other.den + other.num*self.den
    new_den= self.den*other.den

    return '{}/{}'.format(new_num,new_den)

   def __sub__(self,other):
    new_num = self.num*other.den - other.num*self.den
    new_den= self.den*other.den

    return '{}/{}'.format(new_num,new_den)

   def __mul__(self,other):
      new_num =self.num*other.num
      new_den =self.den*other.den

      return'{}/{}'.format(new_num,new_den)

   def __truediv__(self,other):
      new_num =self.num*other.den
      new_den=self.den*other.num

      return'{}/{}'.format(new_num,new_den)
      
      

  
fr1=Fraction(3,4)   
fr2=Fraction(1,2)

print(fr1+fr2)
print(fr1-fr2)
print(fr1*fr2)
print(fr1/fr2)




