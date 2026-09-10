# add two number with lambda function
add=lambda a,b:a+b
print(add(89,56))

# write a program in python two find the greatest number in python.
var=lambda a,b: (a,"a is greater than") if a>b else (b,'b is greater than')
print(var(65,70))

# write a program check even or odd in filter list.
def even(num):
    if num%2==0:
        return True
    else:
        return False
lst=[56,78,66,33,43]
var=list(filter(even,lst))
print(var)

# use of filter in lambda:
lst=[45,66,78,87,12,21]
var=filter(lambda x:x<30,lst)
print(list(var))

# find the no is even or odd.
lst=[23,45,44,67,88,90,9]
var=filter(lambda x:x%2==0,lst)
var1=filter(lambda x:x%2!=0,lst)
print(list(var))
print(list(var1))

lst=[23,22,13,11,10]
print(lst)
var=list(map(lambda a:a*2,lst))
print(var)

# use function

lst=[23,22,13,11,10]
print(lst)
def even(num):
    return num*2
var=list(map(even,lst))
print(var)


# write a program to python to take a list a convert all elements in upper case.
name=["shubh,'ram"]
print(name)
def ss(num):
    return num.upper()
var=list(map(ss,name))
print(var)

from functools import *
lst=[23,22,13,11,10]
v=reduce(lambda x,y:x+y,lst)
print(v)

# use map with a simple function to find the sqare of every number in a list
lst=[23,22,13,11,10]
print(lst)
def sqaure(num):
    return num*num
var=list(map (sqaure,lst))
print(var)

# use map() with a lambda function to add 10 to every number in a list;
lst=[24,56,87,56,78]
print(lst)
def add(num):
    return num+10
var=list(map(lambda num:num+10,lst))
print(var)

# use map() with a lambdafunction to convert all names to uppercase
lst=["shubh","shivam"]
print(lst)
var=list(map(lambda a:a.upper(),lst))
print(var)

# use filter with a simple function to find all even numbers from a list
lst=[35,544,66,5677,78]
print(lst)
def even(a):
    return a%2==0
var=list(filter(even,lst))
print(var)

# use filter with a lambda function to find all odd numbers from a list
lst=[35,544,66,5677,78]
print(lst)
var=list(filter(lambda a:a%2!=0,lst))
print(var)

# use filter with a lambda function to find all numbers greater than 30
lst=[45,22,56,75,234,9,66,8,45,8]
print(lst)
var=list(filter(lambda a:a>30,lst))
print(var)

# use reduce with a lambda function to find the sum of all number in a list
from functools import *
lst=[34,56,66,78,98,12]
print(lst)
var=int(reduce(lambda a,b:a+b,lst))
print(var)

# use reduce with a simple function to find the largest number in a list:
from functools import *
lst=[34,56,66,78,98,12]
print(lst)
def largest(a,b):
    return a if a>b else b
var=int(reduce(largest,lst))
print(var)

# use map with a lambda function to find the cube of every numbber a list
lst=[34,65,6,2,67,7,5]
print(lst)
var=list(map(lambda a:a*a*a,lst))
print(var)

# use filter with a lambda function to find all positvie numbers from a list:
lst=[34,-6,55,-66,66,-90]
print(lst)
var=list(filter(lambda a:a>0,lst))
print(var)

# use filter with a simple function to find all prime numbers from a list
lst=[34,11,5,7,46,54]
print(lst)
def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
var=list(filter(is_prime,lst))
print(var)

# use filter with a lambda function to find all words whose length is greatewr than 5.
lst=["shubh","ram","shivam","devansh","hell","hey"]
print(lst)
var=list(filter(lambda word:len(word)>4,lst))
print(var)

# use map with a simple function to convert temperature from celsius to fahrenheit.
lst=[34,54,55,23]
print(lst)
def temperature(a): 
    return (a*1.8)+32
var=list(map(temperature,lst))
print(var)

# use map with a lambda function to convert all integers into strings.
lst=[34,54,55,23]
print(lst)
var=list(map(lambda a:str(a),lst))
print(var)

# use reduce() with a lambda function to find the product of all numbers in a list
from functools import*
lst=[34,54,55,23]
print(lst)
var=int(reduce(lambda a,b:a*b,lst))
print(var)

# use map with a simple function to find the factioiral of every number in a list.
lst=[2,3,5,51,6,7]
print(lst)
def factorail(a):
    fact=1
    for i in range(1,a+1):
        fact*=i
    return fact
var=list(map(factorail,lst))
print(var)

