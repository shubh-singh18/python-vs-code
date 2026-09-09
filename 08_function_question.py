# Prime Number
# Write a function is_prime(n) that checks whether a given number is prime or not. Return True if prime, otherwise False.
def prim(a):
    if a<2:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
print(prim(10))


# Factorial
# Write a function factorial(n) to calculate the factorial of a number using a loop
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
a=int(input("enter a number"))
print(factorial(a))

# Largest Element in a List
# Write a function largest_element(numbers) that finds the largest element in a list without using the max() function

def largest_element(number):
    largest=number[0]
    for num in number:
        if num>largest:
            largest=num
    return largest
a=(34,65,67,60,56,98,61)
print(largest_element(a))

# Second Largest Element
# Write a function second_largest(numbers) that finds the second-largest distinct element without using sort() or max().
def second_largest(number):
    largest=number[0]
    second=number[0]
    for num in number:
        if num>largest:
            second=largest
            largest=num
        elif num>second and num!=second:
            second=num
    return second
a=(10,66,756,35)
print(second_largest(a))


# Count Vowels
# Write a function count_vowels(text) that counts the number of vowels in a given string. 
# The function should handle both uppercase and lowercase letters.
def count_vowels(text):
    count=0
    for ch in text:
        if ch.lower() in "aieou":
            count+=1
    return count
a=input("enter a letter")
print(count_vowels(a))


# Reverse a String
# Write a function reverse_string(text) that reverses a string without using [::-1].
def reverse_string(text):
    rev=""
    for i in text:
        rev=i+rev
    return rev
print(reverse_string("shivam"))


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
fibonacci(15)


# Student Marks and Grade
# Write a function calculate_result(marks) that takes a list of marks and calculates:

# Total marks
# Percentage
# Grade

def calculate_result(marks):
    total=0
    for num in marks:
        total=total+num
    percentage=total/5

    if percentage>=90 and percentage<=100:
        print("grade A+")
    elif percentage>=80 and percentage<=90:
        print("grade A")
    elif percentage>=70 and percentage<=80:
        print("grade B+")
    elif percentage>=60 and percentage<=70:
        print("grade B")
    elif percentage>=50 and percentage<=60:
        print("grade c+")
    elif percentage>=40 and percentage<=50:
        print("grade c")
    elif percentage>=30 and percentage<=40:
        print("grade E")
    else:
        print("fail")
    return  percentage,total
marks=(78,67,76,90,78)
print(calculate_result(marks))

# Employee Salary Calculator
# Write a function employee_salary(basic_salary) to calculate an employee's gross salary using:

# HRA = 20% of basic salary
# DA = 10% of basic salary
# Gross Salary = Basic + HRA + DA
# Menu-Driven Program Using Function
def employee_salary(basic_salary):
    gross_salary=0
    HRA=basic_salary*20/100
    DA=basic_salary*10/100
    gross_salary=HRA+DA+basic_salary
    return gross_salary
print(employee_salary(200000))

# Check Positive, Negative or Zero
def check_number(num):
    if num>0:
        return "positive"
    elif num<0:
        return "negative"
    else:
        return "zero"
print(check_number(0))

# Write a function to find the square of a number.
def square(num):
    return num*num
print(square(9))

# Write a function to check whether a number is even or odd.
def check_wether(num):
    if num%2==0:
        return "even number"
    else:
        return "odd number"
print(check_wether(90))


# Write a function to calculate the average of three numbers.
def average(a,b,c):
    return (a+b+c)/3
print(average(89,78,90))


# Write a function to find the largest of two numbers.
def largest(a,b):
    if a>b:
        return "a is largest"
    else:
        return "b is largest"
print(largest(780,90))

# Write a function to count the number of elements in a list.

def count_elemnts(number):
    count=0
    for num in number:
        count=count+1
    return count
number=(56,76,34,67,89,122,789,998,78)
print(count_elemnts(number))


# Write a function to calculate the sum of all elements in a list.
def calculate(number):
    sum=0
    for num in number:
        sum=sum+num
    return sum
number=(56,78,99,60,89)
print(calculate(number))

# Write a function to calculate the sum of all elements in a list.
def calculate(number):
    smallest=number[0]
    for num in number:
        if num<smallest:
            smallest=num
    return smallest
number=(89,80,57,76)
print(calculate(number))

# Write a function to count positive and negative numbers in a list.
def count(number):
    positive=0
    neagtive=0
    for num in number:
        if num>0:
          positive=positive+1
        elif num<0:
            neagtive=neagtive+1
    return neagtive,positive
number=(45,66,-88,-86)
positive,negative=(count(number))
print(positive)
print(negative)

# write a function that accepts a list of number and return the sum, average ,largest number ,and smallest number.display all four results
def all(number):
    total=0
    largest=number[0]
    smallest=number[0]
    for num in number:
        total=total+num
        if num>largest:
            largest=num
        elif num<smallest:
            smallest=num
    average=total/5
    return total,average,largest,smallest
number=(78,89,67,87,89)
print(all(number))

# factorail
def factorial(number):
    fact=1
    for i in range(1,number+1):
        fact=fact*i
    return fact
print(factorial(5))


# table
def table(num):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)
a=int(input("enter a table"))
table(a)

def table(num):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)
for  i in range(1,6):
    table(i)
    print()

# add number with lambda function
add=lambda a,b:a+b
print(add(45,67))


var=lambda a,b : a if a>b else b
print(var(67,87))


var=lambda a: a*a
print(var(6))

def even(num):
    if num%2==0:
        return True
    else:
        return False
lst=[45,67,56,32,56]
var=list(filter(even,lst))
print(var)

lst=[23,445,65,67,22,14,126]
var=filter(lambda a: a%2==0,lst)
var1=filter(lambda a:a%2!=0,lst)
print(list(var))
print(list(var1))

lst=[34,56,46,75,12,13]
var=filter(lambda a: a>50,lst)
print(list(var))
lst=[34,12,134,6]
print(lst)
var=list(map(lambda a:a*a,lst))
print(list(var))

lst=[1,43,45,556,6,61]
print(lst)
def sqaure(n):
    return n*2
var=list(map(sqaure,lst))
print(var)

from functools import*
lst=[34,54,56,67]
def add(a,b):
    return a+b
var=reduce(add,lst)
print(var)

lst=[34,54,566,677]
print(lst)
def square(a):
    return a*a
var=list(map(square,lst))
print(var)

lst=[45,64,65]
print(lst)
var=list(map(lambda a:a+10,lst))
print(list(var))

import modules1
print(modules1.add(23,45))
print(modules1.sub(80,45))

f=open("hello.txt","w")
print(f.write("hello badu"))
f.close







