# question1-> Safe Division Calculator

# Write a Python program that takes two numbers from the user and performs division.

# Requirements:
# - Use try-except.
# - Handle ValueError if the user enters a non-numeric value.
# - Handle ZeroDivisionError if the second number is 0.
try:
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    print(a/b)
except ValueError:
    print("please enter a numeric value")
except ZeroDivisionError:
    print("the zero division erro")


# question2-> Student Marks Validator

# Write a program that takes marks from the user.

# Requirements:
# - Marks must be between 0 and 100.
# - If the user enters a non-numeric value, handle ValueError.
# - If marks are less than 0 or greater than 100, use raise to generate a ValueError.
# - Display a suitable message for invalid marks.
try:
    marks=int(input("enter a markss"))
    if marks>0 & marks<100:
        raise ValueError("please enter marks 0 between 100")
    print(marks)
except ValueError:
    print("please enter a numericx value")


# question3->. Bank Withdrawal System

# Create a simple bank withdrawal program.

# Requirements:
# - Set an account balance of ₹10,000.
# - Take the withdrawal amount from the user.
# - If the amount is greater than the balance, use raise to generate an Exception.
# - Handle the exception using try-except.
# - If the withdrawal is successful, display the remaining balance.
balance=10000
try:
    amount=int(input("enter a balance"))
    if amount>balance:
        raise Exception("insfullient balance")
    balance=balance-amount
    print("withdrawl successfully")
    print(balance)
except Exception as t:
    print("error",t)