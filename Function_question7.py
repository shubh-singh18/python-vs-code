# Fibonacci Series
# Write a function fibonacci(n) that returns the first n terms of the Fibonacci series
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c
fibonacci(18)