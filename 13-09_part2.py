# if statement
age=20
if age>18:
    print("you can vote")

# else statement
age=2
if age>18:
    print("vote")
else:
    print("not vote")
# if-else else statement
# used when thre are multiple condition
marks=78
if marks>90:
    print("A")
elif marks>80:
    print("B")
elif marks>70:
    print("C")
else:
    print("fail") 

# Nested if-else statemnt
age=70
member=True
if age>60:
    if member:
     print("30 senior person")
    else:
        print("20 senior person")
else:
    print("not sicount senoir ")

# leap year question...
year=int(input("enter a year"))
if (year%4==0) and (year%100!=0) or (year%400==0):
    print("this year is leap year")
else:
    print("this year is not a leap year")

# check letter is vowels or not
letter=(input("enter a letter"))
if letter in "aieou":
    print("yes")
else:
    print("no")

side1=int(input("enter a first side"))
side2=int(input("enter a second side"))
side3=int(input("enter a thrid side"))
if (side1+side2>side3) and (side1+side3>side2) and (side2+side3>side1):
    print("yes it is triangle")
else:
    print("no it is no triangle")


# for loops is used too repeat a block of code a sppecific number of time.
for i in range(1,101,2):
    print(i)


name="shubhsingh"
for i in name:
    print(i)

# print a table
a=int(input("enter a table"))
for i in range(1,11):
    print(i*a)

# print a mutiple table
a=int(input("enter a table"))
for i in range(1,a+1):
    print(i)
    for j in range(1,11):
        print(i*j)

a=5
for i in range(1,11):
    print(i*a)

# find the factrial number
a=int(input("enter a number"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)

# find the sum of number
a=int(input("enter a number"))
sum=0
for i in range(1,a+1):
    sum=sum+i
print(sum)

# find the sum of even number
a=int(input("enter a number"))
sum=0
for i in range(1,a+1):
    if i%2==0:
        sum=sum+i
print(sum)

# find the sum of odd number
a=int(input("enter a  number"))
sum=0
for i in range(1,a+1):
    if i%2!=0:
        sum=sum+i
print(sum)
# print the even number or not
a=int(input("enter a number"))
count=0
if (a<=1):
    count=count+1
else:
    for i in range(2,a):
        if a%i==0:
            count=count+1
if count==0:
    print("prime")
else:
    print("not prime")


# given a string use a for loop to count how many vowels in contains
text=input("enter a text")
count=0
for ch in text:
    if ch.lower() in "aieou":
        count=count+1
print(count)

# write a program a string using a for loop without using slicing
text=input("enter a text")
rev=""
for i in range(len(text)-1,-1,-1):
    rev+=text[i]
print(rev)

rows=5
for i in range(1,rows+1):
    print("*"*i)


# list main positvie aur negative numbers count kare
number=[34,43,-43,54,-56]
positve=0
negative=0
for num in number:
    if num>0:
        positve+=1
    if num<0:
        negative+=1
print(positve)
print(negative)

# list ka average calaculate karo
number=[34,65,56,67,56]
total=0
count=0
for num in number:
    total+=num
    count+=1
average=total/count
print(average)

# list main duplicate values find karo
number=[45,45,67,67,74,545,57]
for num in number:
    if number.count(num)>1:
        print(num)

# second largest number in a list
number=[455,675,57,657]
largest=number[0]
second=number[0]
for num in number:
    if num>largest:
        second=largest
        largest=num
    elif num>second and num!=second:
        second=num
print(num)

# find the prime number in a list
number=[5,11,2334,4566,77]
for num in number:
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num)

# 1 to 101 prime number find karo
for num in range(1,101):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num)

# while Loop 
a=int(input("enter a number"))
i=0
while(i<a):
    i+=1;
    print(i)

# oddd number
a=int(input("enter a  number"))
i=1
sum=0
while(i<a):
    sum+=i
    i+=2
    print(sum)

# jump statement
# In python , jump statement are used to change the normal flow of execution in loops or functions.the main jump statement are:

# Break
# The break statement immediately terminates the loop.
