#1. Safe Division Calculator

#Write a Python program that takes two numbers from the user and performs division.

#Requirements:
#- Use try-except.
#- Handle ValueError if the user enters a non-numeric value.
#- Handle ZeroDivisionError if the second number is 0.
#- Print a suitable error message for each exception.

#try:
#    a=int(input("enter a number"))
#    b=int(input("enter a number"))
#    print(a/b)

#except ValueError:
#    print("error,non-numeric value")
#except ZeroDivisionError:
#    print("zero cannot divide ")
    
    

#2. Student Marks Validator

#Write a program that takes marks from the user.

#Requirements:
#- Marks must be between 0 and 100.
#- If the user enters a non-numeric value, handle ValueError.
#- If marks are less than 0 or greater than 100, use raise to generate a ValueError.
#- Display a suitable message for invalid marks.

#try:
#    marks=int(input("enter a marks"))
#    if marks<0 or marks>100:
#        raise ValueError("error,enter a marks between 0 to 100")
#    print(marks)
#except ValueError as f:
#    print(f)

#try:
#    marks=float(input("enter a numberr"))
#    if marks<0 or marks>100:
#        raise ValueError("error,enter a marks must betweeen 0 to 100")
#    print(marks)
#except ValueError as f:
#    print(f)



#3. Bank Withdrawal System

#Create a simple bank withdrawal program.

#Requirements:
#- Set an account balance of ₹10,000.
#- Take the withdrawal amount from the user.
#- If the amount is greater than the balance, use raise to generate an Exception.
#- Handle the exception using try-except.
#- If the withdrawal is successful, display the remaining balance.


#Balance=10000
#try:
#    amount=int(input("enter a amount"))
#    if Balance<amount:
#        raise Exception("error,invalid balance")
#    Balance=Balance-amount
#    print("withdrawal successfully")
#    print(Balance)
#except Exception as f:
#    print(f)


#4. Age Eligibility Checker

#Write a program that takes a person's age.

#Requirements:
#- Convert the input into an integer.
#- Handle ValueError if the user enters invalid data.
#- If the age is less than 18, use raise to generate an exception with the message "Not eligible".
#- If the age is 18 or above, print "Eligible

#try:
#   age=int(input("enter a age"))
#    if age<18:
 #       raise Exception("error,not eligible")
#    print("eligible")
#except Exception as f:
#    print(f)


#5. File Handling with Exception Handling

#Write a program to read data from a file named "student.txt".

#Requirements:
#- Use try-except-finally.
#- Handle FileNotFoundError if the file does not exist.
#- If the file exists, print its contents.
#- Use finally to print "File operation completed".

#try:
#    with open("student7.txt","r")as f:
#        print(f.read())
#except FileNotFoundError:
#    print("error,file does not exist")
#finally:
#    print("file operation completed")


#6. Login System

#Create a simple login system.

#Use:
#username = "admin"
#password = "python123"

#Take username and password from the user.

#Requirements:
#- If the username or password is incorrect, use raise to generate an exception.
#- Handle the exception using try-except.
#- If both are correct, print "Login Successful".
#- Display an appropriate error message for invalid login.

#username1="shubh"
#password1=123
#try:
#    username=input("enter a name")
#    password=int(input("enter a passsword"))
#    if username1!=username or password1!=password :
#        raise Exception("error,incorrect password and username")
#    print("login successful")
#except Exception as f:
#    print("invalid",f)

#7. Custom Exception for Age

#Create a custom exception named AgeError.

#Requirements:
#- Create AgeError by inheriting from Exception.
#- Take age from the user.
#- If age is less than 18, raise AgeError with the message "Age must be 18 or above".
#- Handle AgeError using try-except.
#- If the age is valid, print "You are eligible".

#class AgeError(Exception):
#    pass
#try:
#    age=int(input("enter a age"))
#    if age<18:
#        raise AgeError("error,age must be 18 or above")
#    print("you are eligible")
#except Exception as f:
#    print(f)





#8. Custom Exception for Insufficient Balance

#Create a custom exception named InsufficientBalanceError.

#Requirements:
#- Set balance = 5000.
#- Take withdrawal amount from the user.
#- If withdrawal amount is greater than balance, raise InsufficientBalanceError.
#- Handle the custom exception using try-except.
#- If the transaction is successful, display the remaining balance

#class Insufficientbalance(Exception):
 #   pass
#Balance=5000
#try:
 #   amount=int(input("enter a amount"))
 #   if Balance<amount:
 #       raise Exception("error,InsufficientBalanceError")
  #  Balance=Balance-amount
  #  print("transaction is successful")
  #  print(Balance)
#except Insufficientbalance as f:
#    print(f)
#except ValueError:
#    print("error,please enter a amount")

#9. Calculator with Finally

#Create a calculator that performs addition, subtraction, multiplication, and division.

#Requirements:
#- Take two numbers from the user.
#- Take an operator (+, -, *, /).
#- Handle invalid numeric input using ValueError.
#- Handle division by zero using ZeroDivisionError.
#- Use finally to print "Calculator execution completed".

#try:
 #   a=int(input("enter a number"))
 #   b=int(input("enter a number"))
 #   operator=input("enter a(+,-,/,*)")
 #   if operator=="+":
 #       print(a+b)
 #   elif operator=="-":
 #       print(a-b)
 #   elif operator=="*":
 #       print(a*b)
 #   elif operator=="/":
  #      print(a/b)
  #  else:
   #     print("invalid operator")
#except ValueError:
 #   print("error,invalid numeric")
#except ZeroDivisionError:
 #   print("zero cannot divide")
#finally:
 #   print("calculator excuption completed")


#10. Student Registration System

#Create a simple student registration program.

#Take the following inputs:
#- Student name
#- Age
#- Marks

#Requirements:
#- Age and marks must be numeric.
#- Age must be between 18 and 60.
#- Marks must be between 0 and 100.
#- Use raise to generate appropriate

try:
    name=str(input("enter a name"))
    age=int(input("enter a age"))
    marks=int(input("enter a marks"))
    if age<18 or age>60:
        raise Exception("error,age must be between 18 and 60")
    if marks<0 or marks>100:
        raise Exception("error,marks must be between 0 and 100")
    print("student registration pragram successfully ")
    print(name)
    print(age)
    print(marks)
except Exception as f:
    print(f)

