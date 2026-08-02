#question1-> #print a number 

a=int(input("enter a number"))
i=5
while(i<=a):
    i+=1
    print(i)

#question2->print a odd numbers use while loop

a=int(input("enter  a number"))
i=1
sum=0
while(i<=a):
    print(i)
    i+=2

#question3-> using random number guss

import random
secert=random.randint(1,15)
a=int(input("enter a number from 1 to 15"))
while a!=secert:
    if a<secert:
        print("a is the less then secert number",secert)
    else:
        print("a is the greater then secert number",secert)
        a=int(input("enter a number from 1 to 15"))
print("you guss a correct number")

#question4->ATm ek program banao jisme initial balance ₹10000 ho . user se withdraw amount lo . Agar balance sufficient ho to amount decuct karo aur naya balance dikho. har transaction  ke baad pucho "aur paise niklana hai(yes/no),jab tak uesr "yes"
#bole tab tak program chlata rahe

balance=10000
print("balance",balance)
while True:

    amount=int(input("enter a amount you withdraw"))
    if amount<=balance:
       balance=balance-amount
       print("withdraw successful")
       print("avaible balance",balance)
    else:
        print("Insufficient balance")
    again=input("withdraw again?(yes/no),")
    if again.lower()!="yes":
     b=balance-amount
     print(b)
     print("thank you")
     break;

#question5->Login system
#ek program banao jisme.
#username"admin"aur password"1234"ho.user se username aur password tab tak input lo jab tak dono sahi na ho jaye sahhi hone par "login successful" print


user_name="hello"
password=111
while True:
 name=str(input("enter a user_name"))
 b=int(input("enter a password"))
 if user_name==name and password==b :
  print("login successfully")
  break
 else:
  print("worng detail file,please try again")
  continue
 





