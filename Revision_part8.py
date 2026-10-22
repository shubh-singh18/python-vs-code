
# print a table

a=int(input("enter a table"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)

# find the factorial of number

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

# find the even number sum

a=int(input("enter a number"))
sum=0
for i in range(1,a+1):
    if i%2==0:
        sum=sum+i
print(sum)

# find the sum of odd number

a=int(input("enter a number"))
sum=0
for i in range(1,a+1):
    if i%2!=0:
        sum=sum+i
print(sum)

# print the prime number or not

a=int(input("enter a number"))
count=0
if (a<1):
    count+=1
else:
    for i in range(2,a):
        if (a%i==0):
            count=count+i
if count==0:
    print("prime")
else:
    print("not prime")

# given a string use a for loop to count how many vowels "aieou" it contains 

text=input("enter a letter")
count=0
for ch in text:
    if ch in "aieou":
        count+=1
print(count)

# reverse a string 
# write a program to reverse a string using a for loop without using slicing...

text=input("enter a number")
rev=""
for i in range(len(text)-1,-1,-1):
    rev+=text[i]
print(rev)

# find the largest number

number=[21,23,43,55,76,570,76]
largest=number[0]
for num in number:
    if num>largest:
        largest=num
print(largest)