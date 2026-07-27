# write a program that asks the user for an integer and prints "even" if the number is even and "odd" if it is odd

num=int(input("enter a number"))
if num%2==0:
   print("even number")
else:
   print("odd number")

# write a program that prompts the user for a number and check whether it is positive,negative,or zero using if elif-else statements

num=int(input("enter a number"))
if (num>0):
    print("Number is positive")
elif (num<0):
    print("Number is negative")
else:
    print("Number is zero")

#write a program that takes a person age as input.if the age is 18 or older, display "eligible to vote", otherwise, display "not eligible to vote".
 
age=int(input("enter a age"))
if (age>=18):
    print("Eligible to vote")
else:
   print("Not Eligible to vote")

# write a program that accept two number from user and uses conditional statements to determine and print the larger value.

a=int(input("enter a first number"))
b=int(input("enter a second number"))
if a>b :
   print(a,"a is a larger number")
elif a<b :
   print(b,"b is a larger number")
else:
  print("a and b are equal number")


#write a python program that takes a numerial score (0 to 100) and print the corresponding grade 'A' for 90+,'B' for 80-89,'c' for 70-79,'D' for 60-69 and f for below 60.

marks=int(input("enter a marks"))
if marks>=90:
    print("grade is a A")
elif marks>=80:
 print("grade is a B")
elif marks>=70:
   print("grade is a c")
elif marks>=60:
   print("grade is a D")
else:
   print("grade is a fail")

#Write a program to determine whether a give year entered by the user is a leap year.(A year is a leap year if it is divide by 4,but century years must also be divide by 400)

year=int(input("enter a year"))
if year%4==0 and year%100!=0 or year%400==0:
    print("This year is a leap year")
else:
    print("This year is not a leap year")


#write a python program thaing acts as a traffic light simulator.It should accept"Red","Yello"or "green", and print "stop","slow down", or "go" respectively . print "Invalid"for any other input.

color=str(input("enter a traffic light"))
if color=="red":
    print("stop")
elif color=="yellow":
    print("slow down")
elif color=="green":
    print("go")
else:
    print("invalid")

#write  a python that asks the user for a single letter and checks whether it is  a vowel (a,e,i,o,u) or a constanant making sure to handle both upper and lowercase input.

letter=(input("enter a letter"))
if letter in "a,e,i,o,u" .upper():
   print("it is a vowel")
else:
 print("it is a constanant")

#write a python program that takes three side length as input and user conditional logic to verify if they  can successfully form a valid triangle.

side1=int(input("enter a first side"))
side2=int(input("enter a second side"))
side3=int(input("enter a third side"))
if (side1+side2>side3) and(side1+side3>side2)and(side2+side3>side1):
 print("valid side")
else:
 print("invalid side")

# Write a program that stores a master username and password . prompt the user for credentials to report if the login is successful, the password is wrong, or the user does not exist.

master_username="shubhsinghchauhan"
master_password="asusvivobook"
username=input("enter a username")
password=input("enter a password")
if master_username==username:
    print("login successful")
else:
    print("wrong password")