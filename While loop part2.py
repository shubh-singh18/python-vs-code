# question1-> Student marks entry
#ek program banno jisme har student ke marks input lo.Total aur average calculate karo.Har student ke baad pucha."do you want to add anoter student (yes/no)".jab tak user"yes"bole tab tak program chalta rahe.


choice="yes"
while choice== "yes":
    name=input("enter a student name")
    english=int(input("enter a english marks"))
    hindi=int(input("enter a hindi marks"))
    maths=int(input("enter a maths marks"))

    total=english+hindi+maths
    average=total/3
    print("student name",name)
    print("total marks",total)
    print("average marks",average)

    choice=input("do you want to add student(yes/no)?").lower()
    print("program end ")


#question2=> Shopping bill generator
#ek program banno jisme product ka naam aur price input lo. sabhi product ka total bill calculate  karo. har product ke baad pucho."add another product?("yes/no")".
#jab user"no"bole tab fianl bill print karo


total=0
choice="yes"
while choice=="yes":
    product=input("enter a product name")
    price=float(input("enter a product price"))
    total=total+price
    choice=input("add another producr?(yes/no)").lower()
    print("/.final bill")
    print("total bill",total)

#question3=>write a python program to create a simple student result management system display  the following menu repeatedly .
#enter marks
#check result 
#exit 
#requirements
#assume total marks are out of 100. if marks are 40 or above,display"pass" otherwise,display"fail".contain showing the menu until the user choose exit.if the user enters an invalid option,display"invalid choice"?


while True:
    a=input("enter a student name")
    marks=float(input("enter a student marks"))
    b=input("check result(yes/no)")
    if( b=="yes"):
       print("result")
    if (40<marks and b=="yes"):
        print("pass")
    elif (40>marks and b=="yes"):
        print("fail")
    else:
        print("exit")
        break

#Movie ticket booking system
#program statement
#write a python program for a simple movies ticket booking system dispaly the following menu:
#book ticket
# chek availble seats
# exit
# requirements
# initially there are 20 seats aviable .if the user selects book ticket , ask how many tickets they want if enoungh seats are avialble book the tickets and reduce  the availble seats otherwise diaplay seats not availble continue until the user selects exit handle invalid menu choices


total=20
print("total ticket",total)
while True:
 a=int(input("Number of ticket book"))
 if(total>=a):
  print("ticket is book")
 else:
      print("ticket is not available")
      break
 b=(total-a)
 print("avilable ticket",b)
 
c=(input("Invalid")) 
print(c)



        