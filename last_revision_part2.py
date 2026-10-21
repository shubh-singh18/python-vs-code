# check number is even or odd
def even(num):
    if num%2==0:
        return("enven")
    else:
        return("oddd")
d=even(90)
print(d)

# Prime Number
# Write a function is_prime(n) that checks whether a given number is prime or not. Return True if prime, otherwise False.
def prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%2==0:
         return False
    return True
a=prime(110)
print(a)


# Factorial
# Write a function factorial(n) to calculate the factorial of a number using a loop
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
a=factorial(5)
print(a)

# Largest Element in a List
# Write a function largest_element(numbers) that finds the largest element in a list without using the max() function.
def largest(number):
    largest=number[0]
    for num in number:
        if num>largest:
            largest=num
    return largest
lst=(10,20,344,45)
print(largest(lst))

# Count Vowels
# Write a function count_vowels(text) that counts the number of vowels in a given string. 
# The function should handle both uppercase and lowercase letters.
def count_vowels(text):
    count=0
    for ch in text:
        if ch.lower() in "aieou":
            count+=1
    return count
text=input("entera a text")
print(count_vowels(text))


def reverse_count(text):
    rev=""
    for i in text:
        rev=i+rev
    return rev
teat=input("ente a text")
print(reverse_count(teat))

# Fibonacci Series
# Write a function fibonacci(n) that returns the first n terms of the Fibonacci series
def fibonnaci(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c
fibonnaci(18)


# Write a function to calculate the sum of all elements in a list.
def calculate(number):
    sum=0
    for num in number:
        sum=sum+num
    return sum
number=[10,20,30]
print(calculate(number))


# Write a function to find the largest of two numbers.
def largest(a,b):
    if a>b:
        return " a islargest"
    else:
        return "b issmalllest"
print(largest(34,567))

def add(*number):
    print(sum(number))
add(10,20)
add(10,20,30,40)

class student:
    name="shubh"
s1=student
print(s1.name)

# __init__
class student:
    def __init__(self,name):
        self.name=name
s1=student("shubh")
print(s1.name)


class car:
    wheels=7
    def __init__(self,color):
        self.color=color

# classs method
class a:
    def dog(self):
        print("dog")
class b(a):
    def cat(self):
        print("cat")
aa=b()
aa.dog()
aa.cat()

# multiple inheritance
class a:
    def display(self):
        print("this is chlid")
class b:
    def show(self):
        print("this second child")
class c(a,b):
    pass
oo=c()
oo.display()
oo.show()

class a:
    def display(self):
        print("thsio is grandfather")
class b(a):
    def show(self):
        print("this is father")
class c(b):
    pass
obj=c()
obj.display()
obj.show()


# hybrid 
class a:
    def method(self):
        print("mehod of class a")
class b(a):
    def method_b(self):
        print("method of class b")
class c(a):
    def method_c(self):
        print("methopd of class c")

class d(b,c):
    def method_d(self):
        print("method of class d")
obj=d()
obj.method()
obj.method_b()
obj.method_c()
obj.method_d()

# compile time
class a:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
obj=a()
obj.add(10,20,30)

class a:
    def add(self,*args):
        print(sum(args))
obj=a()
obj.add(10,20)
obj.add(10,20,30)


class a:
    def add(self,*args):
        print(sum(args))
o=a()
o.add(10,34,54)
o.add(10,23)

# 
class a:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,other):
        return self.marks+other.marks
o=a(34)
oq=a(90)
print(o+oq)

# 
class a:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b):
        print(a-b)
obj=a()
obj.add(20,200)


# abstract method
from abc import ABC, abstractmethod
class anminal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(anminal):
    def sound(self):
        print("dog")
a=Dog()
a.sound()


# Access modifier
# Access modifer define or indicate how the variable or method of a class can be acccesss otside from the class
def genrator():
    yield 1
    yield 2
x=genrator()
print(next(x))
print(next(x))

def genrator():
    yield 1
    yield 2
x=genrator()
print(next(x))
print(next(x))



a=int(input("enter a number"))
count=0
if a<2:
    count=count+1
else:
    for i in range(2,a):
        if a%i==0:
            count=count+1
if count==0:
    print("prime")
else:
    print("not primme")

a=int(input("enter a number"))
sum=0
for i in range(1,a+1):
    if i%2==0:
        sum=sum+i
print(sum)


a=int(int(input("enter a number")))
sum=0
for i in range(1,a+1):
    sum=sum+i
print(sum)

for num in range(1,101):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
      print(num)

for num in range(1,101):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
      print(num)

number=[1,2233,44,344,11,5,7]
for num in number:
 count=0
 for i in range(1,num+1):
    if num%i==0:
        count+=1
 if count==2:
     print(num)

number=[11,23,22,44]
for num in number:
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num)


a=10.8
b=int(a)
print(type(b))

a=200
b=300
c=400
obj="a" if a>b and a>c else "b" if b>c else "c"
print(obj) 


a=int(input("enter a number"))
i=6
while (i<a):
    i+=1;
    print(i)

a=int(input("enter a number"))
i=6
while(a<i):
    i+=1
    print(i)

a=int(input("enter a number"))
i=1
sum=0
while i<=a:
    sum+=i
    i+=2
print(sum)

