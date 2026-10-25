# # # total keyword find
# # import keyword
# # print(keyword.kwlist)

# # # type function
# # a=23
# # print(type(a))

# # # swap two number
# # a=20
# # b=21
# # a,b=b,a
# # print(a,b)

# # # swap two number with help of c
# # a=11
# # b=23
# # c=a
# # a=b
# # b=c
# # print(a,b)

# # # swap two number with other method
# # a=23
# # b=90
# # a=a+b
# # b=a-b
# # a=a-b
# # print(a,b)


# # # print add two number 
# # a=33
# # b=34
# # print(a+b)

# # # Implicit casting
# # a=10
# # b=30.5
# # c=a+b
# # print(c)
# # print(type(c))

# # # explicit casting 
# # a=23
# # print(a)
# # print(type(a))
# # a=float(23)
# # print(type(a))

# # Write a program to print the first 5 characters of a string using slicing.
# # a="shubhsingh"
# # print(a[:5])

# # Write a program to print the last 4 characters of a string using slicing
# # a="shubhsingh"
# # print(a[-4:])


# # # Write a program to reverse a string using slicing.
# # a="shubhsingh"
# # print(a[::-1])


# # Write a program to print every second character of a string using slicing
# # a="shubhsingh"
# # print(a[0:9:2])


# # Write a program to print characters from index 2 to index 6 using slicing.
# # a="shubhsingh"
# # print(a[2:6])


# # Write a program to check whether a string is a palindrome using slicing.
# # a="shubhsingh"
# # if a==a[::-1]:
# #     print("palindrome")
# # else:
# #     print("not palindrome")

# # # "PythonProgramming" me se sirf Python slicing se print karo.
# # a="pythonprogramming"
# # print(a[0:6])


# # # "DataAnalytics" me se sirf Analytics slicing se print karo
# # a="dataanalytics"
# # print(a[4:13])

# # # Write a program to print the string in reverse order with every second character skipped.
# # a="dataanalytics"
# # print(a[::-2])


# # User se ek string input lo aur slicing ka use karke uski first half aur second half print karo.
# # text=input("enter a string")
# # mid=len(text)//2
# # print("first half",text[:mid])
# # print("second half",text[mid:])

# # check two number greater number find
# a=102
# b=23
# c=a if a>b else b
# print(c)

# # check three number greater number find
# a=230
# b=240
# c=25
# d=a if a>b else b if b>c else c
# print(d)

# # check four number greater number find
# a=10
# b=20
# c=30
# d=4
# f=a if a>b else b if b>c else c if c>d else d
# print(f)

# # check person can vote or not 
# age=2
# print("vote" if age>18 else "not vote")


# # check number is positive ,negative,zero
# a=int(input("enter a number"))
# print(a>0,"Positve")
# print(a<0,"Negative" )
# print(a==0,"Zero")


# # check two number is greater number
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# if (a>b):
#     print("a number is greater number")
# elif (a<b):
#     print("b is number is greater number")
# else:
#     print("both number are equall")

# # leap year
# year=int(input("enter a year"))
# if (year%4==0 and year%100!=0)or (year%400==0):
#     print("this is a leap year")
# else:
#     print("this is not a leap year ")

# # vote 
# a=int(input("enter a number"))
# if (a>18):
#     print("you can vote")
# else:
#     print("you can not a vote")

# # triangle question 
# side1=int(input("enter a side"))
# side2=int(input("enter a side"))
# side3=int(input("enter a side"))
# if(side1+side2>side3)and(side1+side3>side2)and(side2+side3>side1):
#     print("valid side")
# else:
#     print("invalid side")

# # vowel question 
# letter=(input("enter a letter"))
# if letter in "aieou":
#     print("vowel")
# else:
#     print("not a vowel")


# # traffic light question
# color=str(input("enter a string"))
# if(color=="red"):
#     print("stop")
# elif (color=="yello"):
#     print("slow down")
# elif (color == "green"):
#     print("go")
# else:
#     print("invalid")

# # 
# # for loop
# for i in range(1,5):
#     print(i)

# # 
# fruits=["Apple","Banana","Mango"]
# for i in fruits:
#     print(i)

# # even number
# for i in range(2,101,2):
#     print(i)

# # odd
# for i in range(1,101,2):
#     print(i)

# # list
# name="shubhsinghchauhan"
# for i in name:
#     print(i)

# # table
# a=int(input("enter a number"))
# for i in range(1,11):
#  print(a,"*",i,"=",a*i)


# factorial
# a=int(input("enter a numbeer "))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

# find the sum of number
# a=int(input("enter a number"))
# sum=0
# for i in range(1,a+1):
#     sum=sum+i
# print(sum)

# find the sum of even number
# a=int(input("entrer a number"))
# sum=0
# for i in range(1,a+1):
#     if i%2==0:
#         sum=sum+i
# print(sum)

# find the sum of odd number
# a=int(input("enter a number"))
# sum=0
# for i in range(1,a+1):
#     if i%2!=0:
#         sum=sum+i
# print(sum)

# # print the prime number or not
# a=int(input("enter a number"))
# count=0
# if (a<=1):
#     count=count+1
# else:
#     for i in range(2,a):
#         if a%i==0:
#             count=count+1
# if count==0:
#     print("prime")
# else:
#     print("not prime")

# given a string use a for loop to count how many vowels (a,i,e,o,u) it contains..
# text=input("enter a number")
# count=0
# for ch in text:
#     if ch.lower() in "aieou":
#         count+=1
# print(count)

# reverse a string
# a=input("enter a number")
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev+=a[i]
# print(rev)

# find the largest nummber
# number=[12,21,34,54,67,76,45,97,56]
# largest=number[0]
# for num in number:
#     if num>largest:
#         largest=num
# print(largest)


# multiplication table..
# a=int(input("enter a table"))
# for i in range(1,a+1):
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)

# list main smallest number find karo... or largest number find karo...
# number=[65,78,33,22,34,98]
# largest=number[0]
# smallest=number[0]
# for i in number:
#     if i>largest:
#         largest=i
#     if i<smallest:
#         smallest=i
# print(largest)
# print(smallest)

# list mein positive aur negative number count kare..
# number=[33,5,-57,87,23,-87,56,-34]
# positive=0
# negative=0
# for num in number:
#     if num>0:
#         positive+=1
#     if num<0:
#         negative+=1
# print(positive)
# print(negative)

# list ka average calculate karo...
# number=[45,56,78,89,12,43]
# total=0
# count=0
# for num in number:
#     total+=num
#     count+=1
# average=total/count
# print(average)

# list mein duplicate values find karo...
# number=[23,32,23,56,7788,778,667]
# for num in number:
#     if number.count(num)>1:
#         print(num)

# find the prime number in a list 
# number=[21,23,11,55,6644,77,45]
# for num in number:
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         print(num)

# 1 to 101 prime number find karo 
# for num in range(1,101):
#     count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
#     if count==2:
#         print(num)

# second largest number in a list
# number=[23,34,45,5,64,33,3432]
# largest=number[0]
# second=number[0]
# for i in number:
#     if i>number:
#         second=largest
#     elif i>second and i!=largest:
#         second=i
# print(second)

# print a table
# a=int(input("enter a table"))
# for i in range(1,11):
#     print(a,"*",i,"=",a*i)

# find the factorial of number
# a=int(input("enter a number"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

# find the sum of number
# a=int(input("enter a number"))
# sum=0
# for i in range(1,a+1):
#     sum=sum+i
# print(sum)

# find the even number sum
# a=int(input("enter a number"))
# sum=0
# for i in range(1,a+1):
#     if i%2==0:
#         sum=sum+i
# print(sum)

# find the sum of odd number
# a=int(input("enter a number"))
# sum=0
# for i in range(1,a+1):
#     if i%2!=0:
#         sum=sum+i
# print(sum)

# print the prime number or not
# a=int(input("enter a number"))
# count=0
# if (a<1):
#     count+=1
# else:
#     for i in range(2,a):
#         if (a%i==0):
#             count=count+i
# if count==0:
#     print("prime")
# else:
#     print("not prime")

# given a string use a for loop to count how many vowels "aieou" it contains 
# text=input("enter a letter")
# count=0
# for ch in text:
#     if ch in "aieou":
#         count+=1
# print(count)

# reverse a string 
# write a program to reverse a string using a for loop without using slicing...
# text=input("enter a number")
# rev=""
# for i in range(len(text)-1,-1,-1):
#     rev+=text[i]
# print(rev)

# find the largest number
# number=[21,23,43,55,76,570,76]
# largest=number[0]
# for num in number:
#     if num>largest:
#         largest=num
# print(largest)

# multiplication table
# a=int(input("enter a number"))
# for i in range(1,a+1):
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)

# print even number from 2 to 10
# for i in range(2,11,2):
#     print(i)


# find the largest and smallest number 
# number=[23,43,56,86,354,87,45,776,56,66]
# largest=number[0]
# smallest=number[0]
# for num in number:
#     if num>largest:
#         largest=num
#     if num<smallest:
#         smallest=num
# print(largest)
# print(smallest)

# list mein positive aur negative number count kare..
# number=[34,-54,56,76,-88]
# positive=0
# negative=0
# for num in number:
#     if num>0:
#         positive+=1
#     if num<0:
#         negative+=1
# print(positive)
# print(negative)

# list ka average calculate karo
# number=[34,465,656,565,434]
# total=0
# count=0
# for num in number:
#     total+=num
#     count+=1
# average=total/count
# print(average)

# list mein duplicated values find karo
# number=[23,544,455,222,23,65,67]
# for num in number:
#     if number.count(num)>1:
#         print(num)

# find the prime number in a list
# number=[343,564,565,34,45,45,45,11]
# count=0
# for num in number:
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#          print(num)

# second largest number in a list
# number=[34,45,67,56,34,87,23]
# largest=number[0]
# second=number[0]
# for i in number:
#     if i>largest:
#         second=largest
#         largest=i
#     elif i>second and i!=largest:
#      second =i
# print(second)


# Jump statements in python 
# in python jump statement are used to change the normal flow of execution in loops or function 
# the main jump statements are:
# break:
# The break statements immediatley terminates the loop.
# for i in range (1,6):
#     if i==4:
#         break
#     print(i)

# continue
# The continue statements skips the current itertiion and moves to the next itertion of the loop
# for i in range(1,6): 
#     if i==3:
#         continue
#     print(i)

# pass
# the pass statements does nothing .it acts as a placeholder where code will be added letter 
# for i in range(1,4):
#     if i==2:
#         pass
#     print(i)

# List in python
# List is a order and mutable connection of mutiple value.
# It can store multiple value
# it is order collection
# list is a mutable can be changed
# it allow duplicate value
# it can store differernt data type value
# change list item
# fruits=["apple","banana","mango"]
# fruits[1]="orange"
# print(fruits)


# using append():Add item at the end
# fruits=["apple","banana"]
# fruits.append("mango")
# print(fruits)

# using inserts ->add item at a specific position
# fruits=["apple","mango"]
# fruits.insert(1,"orange")
# print(fruits)

# using items remove->remove a specific items
# fruits=["apple","mango","banana"]
# fruits.remove("apple")
# print(fruits)

# using pop -> remove items by index (or last item)
# fruits=["applle","banana","mango"]
# fruits.pop()
# print(fruits)
# using sort
# a=[10,20,32,34,43,454,34]
# a.sort()
# print(a)

# reverse()
# a=[21,23,32,35,76,45,87,35]
# a.reverse()
# print(a)

# count()
# a=[23,54,67,46,97,35,35]
# b=a.count(35)
# print(b)

# index)()
# a=[10,34,54,67,55,76,34,87,35,88]
# print(a.index(67))

# clear()
# a=[10,20,30,40,50,60,70,80,90]
# a.clear()
# print(a)

# copy()
# a=[10,20,30,40,50]
# b=a.copy()
# print(a)
# print(b)

# extend()
# a=[10,20,40,30]
# b=[50,60,70,80]
# a.extend(b)
# print(a)

# tuple 
#   The count method is used to count how many times a specified elements appears in a tuple ..
# number=(1,2,3,4,4,4,4)
# print(number.count(4))

# index tuple
# number=(23,43,45,65,677,45,65,67,665)
# print(number.index(43))

# max()
# number=(33,54,676,87,23,88,121)
# print(max(number))

# len()
# number=(454,46,67,232)
# print(len(number))

# sum()
# number=(43,67,23,78,122)
# print(sum(number))

# sorted 
# num=(30,10,20,54)
# print(sorted(num))

# set
# Add() method
# num={12,23,34,45,56,67}
# num.add(100)
# print(num)

# update() method
# num={12,33,43,55}
# num.update([100,200])
# print(num)

# remove() method
# num={10,20,30,40,50}
# num.remove(40)
# print(num)

# discard () method
# num={10,20,30,40,50,60,70,80}
# num.discard(50)
# print(num)

# union method()
# num1={10,20,30}
# num2={30,40,60}
# result=num1.union(num2)
# print(result)


# intersection() method
# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# result=set1.intersection(set2)
# print(result)

# difference() method
# set1={10,20,30,40,50}
# set2={30,40,50,60,70}
# result=set1.difference(set2)
# print(result)

# symmetric_difference() method
# set1={10,20,30,40,50,60,70}
# set2={50,60,70}
# result=set1.symmetric_difference(set2)
# print(result)

# Dictionary in python
# student={
#     "name":"shubhsingh",
#     "age":21,
#     "marks":79
# }
# print(student)

# Accessing values
# student={
#     "name":"shubhsinghchauhan",
#     "age":21
# }
# print(student["name"])
# print(student["age"])

# Adding a new items.
# student={
#     "name":"shubhsinghchauhan"
# }
# student["course"]="python"
# print(student)

# updating value
# student={
#     "name":"shubhsinghchauhan",
#     "age":20
# }
# student["age"]=21
# print(student)

# deleting an items
# student={
#     "name":"shubhsinghchauhan",
#     "age":21
# }
# del student["age"]
# print(student)

# keys
# the keys method is used to return all the keys pressent in a dictionary
# student={
#     "name":"shubh",
#     "age":20,
#     "course":"python"
# }
# print(student.keys())



# get() method in python dictionary
# student={
#     "name":"shubhsinghchauhan",
#     "age":21,
#     "course":"python"
# }
# print(student.get("name"))

# frozen set in python
# number=frozenset([1,2,3,4,5,6])
# print(number)

# calling
# calling means when we want function we call it for use:
# Parameter is a variable used in a function to receive.
# Arguments->They are the value for while calling..
# return statements->function take values from paramenter annd make logic return the value.

# check number is even or odd
# def even(num):
#     if num%2==0:
#         return ("even number")
#     else:
#         return ("odd number")
# dev=even(21)
# print(dev)

#  # Check Positive, Negative or Zero
# def check_number(num):
#     if num>0:
#         return  ("positive")
#     elif num<0:
#         return ("negative")
#     else:
#         return ("zero")
# print(check_number(-21))

# Write a function to find the square of a number.
# def square(num):
#     return num*num
# print(square(5))

# Write a function to check whether a number is even or odd.
# def check_whether(num):
#     if num%2==0:
#         return "even number"
#     else:
#         return "odd number"
# print(check_whether(23))


# Write a function to calculate the average of three numbers.
# def average(a,b,c):
#     return (a+b+c)/3
# print(average(23,34,43))

# Write a function to find the largest of two numbers.
# def largest(a,b):
#     if a>b:
#         return "a is a largest"
#     else:
#         return "b is a largest"
# print(largest(45,65))


# Write a function to count the number of elements in a list.
# def count_elemnts(number):
#     count=0
#     for num in number:
#         count=count+1
#     return count
# number=(34,54,67,87,23,65,89)
# print(count_elemnts(number))

# def sum(number):
#     sum=0
#     for num in number:
#         sum=sum+num
#     return sum
# number=(45,54,56,77,89,34)
# print(sum(number))

# Write a function to count positive and negative numbers in a list.
# def count(number):
#     positive=0
#     negative=0
#     for num in number:
#         if num<0:
#             positive=positive+1
#         elif num<0:
#             negative=negative+1
#     return positive,negative
# number=(32,44,65,78,56)
# positive,negative=(count(number))
# print(positive)
# print(negative)

# # Write a function to calculate the sum of all elements in a list.
# def smallest(number):
#     smallest=number[0]
#     for num in number:
#         if num<smallest:
#             smallest=num
#     return smallest
# number=(354,66,77,556,545,87)
# print(smallest(number))


# use map with a simple function to find the square of every number in a list...
# lst=[2,3,4,5,6,7,8]
# print(lst)
# def sqaure(a):
#     return a*a
# var=list(map(sqaure,lst))
# print(var)

# use map with a lambda function to add 10 to every number in a list
# lst=[34,544,67,34,33,67]
# print(lst)
# var=list(map(lambda a:a+10,lst))
# print(var)

# use map with a lambda function to convert all names to uppercase
# lst="shubhsingh"
# print(lst)
# var=list(map(lambda lst:lst.upper(),lst))
# print(var)

# use filter with a simple function to find all even number from a list.
# lst=[23,45,65,67,87,22,24,26]
# print(lst)
# var=list(filter(lambda a:a%2==0,lst))
# print(var)

# use reducce with a lambda function to find the sum of all number in  a list
# from functools import*
# lst=[44,656,676,24]
# print(lst)
# var=int(reduce(lambda a,y:a+y,lst))
# print(var)

# # use reduce with a simple function to find the largest number in a list
# from functools import*
# lst=[12,34,45,65,778,898,644]
# print(lst)
# def largest(a,b):
#     return a if a>b else b
# var=int(reduce(largest,lst))
# print(var)

# use map with a lambda function to find the cube of every number a list
# lst=[23,5,67,77,68,46]
# print(lst)
# var=list(map(lambda a:a*a*a,lst))
# print(var)

# use filter with a lambda function to find all positive numbers from a list
# lst=[33,45,-67,-7873]
# print(lst)
# var=list(filter(lambda a:a>0,lst))
# print(var)

# use filter with a simple function to find all prime numbers from a list
# def is_prime(num):
#     if num<2:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#         return True 
# lst=[3,4,5,6,7]
# print(list(filter(is_prime,lst)))

# use filter  with a lambda a function to find all words whode length is greater than 5
# lst=["ram","chauhan","shubhsingh"]
# print(lst)
# var=list(filter(lambda word:len(word)>5,lst))
# print(var)



# use map with a simple function to convert temperture from calsius to fahrenhrit.
# lst=[23,343,55,56,99]
# print(lst)
# def tempertaure(a):
#     return (a*1.8)+32
# var=list(map(tempertaure,lst))
# print(var)


# use map with a lambda function to convert all integer into strings
# lst=[23,34,65,676,86]
# print(lst)
# var=list(map(lambda a:str(a),lst))
# print(var)


# file handling
# with open("student101.txt","r")as f:
#     a=f.read()
#     print(a)

# tell()
# f=open("student.txt","r")
# print(f.tell())

# seek()
# f=open("student101.txt","r")
# print(f.seek(3))

# # question1-> Safe Division Calculator

# Write a Python program that takes two numbers from the user and performs division.

# Requirements:
# - Use try-except.
# - Handle ValueError if the user enters a non-numeric value.
# - Handle ZeroDivisionError if the second number is 0.
# try:
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     print(a/b)
# except ValueError:
#     print("please enter a numeric value")
# except ZeroDivisionError:
#     print("the zero division erro")


# question2-> Student Marks Validator

# Write a program that takes marks from the user.

# Requirements:
# - Marks must be between 0 and 100.
# - If the user enters a non-numeric value, handle ValueError.
# - If marks are less than 0 or greater than 100, use raise to generate a ValueError.
# - Display a suitable message for invalid marks.
# try:
#     marks=int(input("enter a markss"))
#     if marks>0 & marks<100:
#         raise ValueError("please enter marks 0 between 100")
#     print(marks)
# except ValueError:
#     print("please enter a numericx value")


# question3->. Bank Withdrawal System

# Create a simple bank withdrawal program.

# Requirements:
# - Set an account balance of ₹10,000.
# - Take the withdrawal amount from the user.
# - If the amount is greater than the balance, use raise to generate an Exception.
# - Handle the exception using try-except.
# - If the withdrawal is successful, display the remaining balance.
# balance=10000
# try:
#     amount=int(input("enter a balance"))
#     if amount>balance:
#         raise Exception("insfullient balance")
#     balance=balance-amount
#     print("withdrawl successfully")
#     print(balance)
# except Exception as t:
#     print("error",t)


# oops
# class 
# class student:
#     name="shubh"
#     age=21
# # object
# s1=student()
# print(s1.name)
# print(s1.age)

# __init__ method
# class
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# # object
# s1=student("shubh",20)
# print(s1.name)
# print(s1.age)


# class attributes
# class student:
#     name="shubh"

# instance attributes
# class student:
#     def __init__(self,name):
#         self.name=name


# self -> ye cuurent object ko refers karta hai
# cls -> ye current class ko refers karta hai 


# instance mathod
# class student:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(self.name)
# s1=student("shubh")
# s1.show()

# class method..
# class student:
#     branch="cse"
#     @classmethod
#     def show(cls):
#         print(cls.branch)
# student.show()


# inheritance
# class parent:
#     def h(self):
#         print("this is parent class")
# class child(parent):
#     def a(self):
#         print("this is child class")
# obj=child()
# obj.h()
# obj.a()

# parametrized constructor
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# non_parametried constructor.
# class student:
#     def __init__(self):
#         print("hello")
# s1=student()

# super function()
# class parent:
#     def show(self):
#         print("parent classs")
# class child(parent):
#     def display(self):
#         super().show()
#         print("child class")
# obj=child()
# obj.display()

# single interitance
# class parent:
#     def show(self):
#         print("this is parent class")
# class child(parent):
#     pass
# obj=child()
# obj.show()

# mutiple interitance
# class parent1:
#     def show(self):
#         print("first parent")
# class parent2:
#     def display(self):
#         print("second parent")
# class child(parent1,parent2):
#     pass
# obj=child()
# obj.show()
# obj.display()

# multilevel interitance
# class parent:
#     def show(self):
#         print("this is grandfather")

# class child1(parent):
#     def dispaly(self):
#      print("this is a father")

# class child2(child1,parent):
#    pass 
# obj=child2()
# obj.show()
# obj.dispaly()

# Hierarchical Inheritance
# class parent:
#     def show(self):
#         print("this is parent class")
# class child1(parent):
#     pass
# class child2(parent):
#     pass
# o=child1()
# o=child2()
# o.show()

# hybrid inheritance 
# class parent:
#     def show(self):
#         print("this is parent class")
# class child1(parent):
#     def display(self):
#         print("this is child1 class")
# class child2(parent):
#     def he(self):
#         print("this is child2 class")
# class son(child1,child2):
#     pass
# obj=son()
# obj.show()
# obj.display()
# obj.he()

# python cannot support method overloading
# class parent:
#     def show(a,b):
#         print(a+b)
#     def show(a,b,c):
# obj=parent()
# obj.show(10,20,30)

# default arguments
# class parent:
#     def add(self,*args):
#         print(sum(args))
# obj=parent()
# obj.add(10,20)
# obj.add(10,20,30)

# method overriding
# class student:
#     def add(self,a,b):
#      print(a+b)
#     def add(self,a,b):
#        print(a-b)
# a=student()
# a.add(23,3)

# use dunder method to add two numbers:
# class student:
#     def __init__(self,marks):
#         self.marks=marks
#     def __add__(self,other):
#         return self.marks+other.marks
# a=student(34)
# b=student(67)
# print(a+b)

# three or more number ko add kar ne liye use dunder method
# class student :
#     def __init__(self,marks):
#         self.marks=marks
#     def __add__(self,other):
#         return student(self.marks+other.marks)
# a=student(200)
# aa=student(34)
# ab=student(67)
# ac=student(67)
# var=aa+ab+ac
# print(var.marks)

# without dender method overloading nhi ho skata hai thik
# class student:
#     def __init__(self,marks):
#         self.marks=marks
# aa=student(45)
# ab=student(67)
# print(aa+ab)


#Abstraction 
# from abc import abstractmethod
# class Animal:
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog:
#     def sound(self):
#         print("dog is bark")
# a=Dog()
# a.sound()

# public access 
# class student:
#     def __init__(self):
#         self.name="shubh"
# a=student()
# print(a.name)

# protected access modifiers


# protected access modifier
# class student:
#     def __init__(self):
#         self.name="shubh"
# class child(student):
#     def display(self):
#         print(self.name)
# obj=child()
# obj.display()

# private access modifier
# class student:
#     def __init__(self):
#         self.__name="shubhsingh"

#     def display(self):
#         print(self.__name)
# a=student()
# a.display()


#getter and setter 
# class student:
#     def __init__(self):
#         self.__marks=0

#     def get_marks(self):
#         return self.__marks

#     def set_marks(self,marks):
#         self.__marks=marks
# a=student()
# a.set_marks(90)
# print(a.get_marks())

# generator
# def a():
#     yield 1
#     yield 3
# x=a()
# print(next(x))
# print(next(x))

# decorator in python
# def decorator(func):
#     def wrapper():
#         print("befor")
#         func()
#         print("after")
#     return wrapper
# @decorator
# def hello():
#     print("hello")
# hello()




# class
# class student:#class
#     name="shubhsingh"
# #object
# s1=student()#object
# print(s1.name)

# __init__
# class student:
#     def __init__(self,name):
#         self.name=name
# s1=student("shubh")
# print(s1.name)

# class attributes
# class student:
#     name="shubhsingh"

# # instance attributes
# class student:
#     def __init__(self,name):
#         self.name=name

# instance method.
# class student:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(self.name)
# s1=student("singh")
# s1.show()

# class method
# class student:
#     branch="cse"
#     @classmethod
#     def show(cls):
#         print(cls.branch)
# student.show()

# inheritance in python
# class parent:
#     def display(self):
#         print("this is a parent class")
# class child(parent):
#     def show(self):
#         print("this is a child class")
# s1=child()
# s1.display()
# s1.show()


# parameterized constructor
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# non_parameterized construct
# class student:
#     def display(self):
#         print("hello")
# s1=student()
# s1.display()


