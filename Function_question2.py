
# Factorial
# Write a function factorial(n) to calculate the factorial of a number using a loop

def Factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("enter a number"))
print(Factorial(n))