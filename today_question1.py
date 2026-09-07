# Write a Python program that takes a number from the user and checks whether it is a prime number or not. Display an appropriate message.
a=int(input("enter a number"))
count=0
if (a<=1):
    count=count+1
else:
    for i in range(1,a+1):
        if (a%2==0):
            count=count+1
if count==0:
    print("this number is prime")
else:
    print("this number is not prime")
    