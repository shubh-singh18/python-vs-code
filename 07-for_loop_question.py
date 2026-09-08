# #question1> print a list
# list="shubhsingh"
# for i in list:
#     print(i)

# print a table
# a=int(input("enter a number"))
# for i in range(1,11):
#     print(i*a)

# find the factorial number
# a=int(input("enter anumber"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

# find the sum number
# a=int(input("enter a number"))
# sum=0
# for i in range(1,a+1):
#     sum=sum+i
# print(sum)

#find the sum of even number
# a=int(input("enter a number"))
# sum=0
# for i in range(1,a+1):
#     if i%2==0:
#         sum=sum+i
#         print(sum)

# print the prime number or not
# a=int(input("enter a number"))
# count=0
# if (a<=1):
#     count=count=1
# else:
#     for i in range(2,a):
#         if a%i==0:
#             count=count=1
# if count==0:
#     print("prime")
# else:
#     print("not prime")

# sum of odd number
# a=int(input("enter a number"))
# sum=0
# for i in range(1,a+1):
#     if i%2!=0:
#         sum=sum+i
# print(sum)

# given a string use a for loop to count how many vowels iaoue it contains
# text=input("enter a number")
# count=0
# for ch in text:
#     if ch.lower() in "aieou":
#         count=count+1
#         print(count)

# reverse string
# write a program to reverse a string using a for loop without using slicing
# text=input("enter a letter")
# rev=""
# for i in range(len(text)-1,-1,-1):
#     rev+=text[i]
# print(rev)

#find the largest number
# given a list of number use a for loop to find the largest number in the list
# number=[23,43,45,64,6644,56]
# largest=number[0]
# for num in number:
#     if num>largest:
#         largest=num
# print(largest)

# fizz buzz
# print number from 1 to 100 for mutiple of :
# 3 print "fizz"
# 5 print "buzz"
# both 3 and 5 print "fizzbuzz" otherwise , print the number itself.

# for i in range(1,101):
#     if i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     elif i%3==0 and i%5==0:
#         print("fizzbuzz")
#     else:
#         print(i)

# ask the user for a number and print its table up to 10
# a=int(input("enter a number"))
# for i in range(1,a+1):
#     print(i)
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)

# rows=5
# for i in range(1,rows+1):
#     print("*"*i)


# list mein even numbers count karo
# number=(23,43,456,45,445,454,55,80)
# for num in number:
#     if num%2==0:
#         print(num)

# # list mein positive our negative numbers count karo .
# number=(34,-54,45,-65,35,-65,45,78)
# positve=0
# negative=0
# for num in number:
#     if num>0:
#         positve+=1
#     if num<0:
#         negative+=1
# print(positve)
# print(negative)


# list ka average calculate karo
# number=(34,53,45,46,76,75,67,90)
# total=0
# count=0
# for num in number:
#     total+=num
#     count+=1
# average=total/count
# print(average)

# list mein duplicate values find karo
# number=(23,44,55,55,23,666,77,56,45,65,65)
# for num in number:
#     if number.count(num)>1:
#         print(num)

# find the prime number in a list:
# number=[2,3,4,5,11,13,68]
# for num in number:
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         print(num)


# # 1 to 101 prime number find  karo
# for num in range(1,101):
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         print(num)

# second largest number in a list:
# number=[10,25,8,67,55]
# largest=number[0]
# second=number[0]
# for i in number:
#     if i>largest:
#         largest=second
#         largest=i
#     elif i>second and i!=largest:
#         second=i
# print(second)


# fibonancci
# def fibonancci(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a)
#         c=a+b
#         a=b
#         b=c
# fibonancci(17)

age=28
if age>=18:
    print("you can vote")

num=23
if num%2==0:
    print("even number")
else:
    print("odd number")

marks=67
if marks>90:
    print("A+")
elif  marks>80:
    print("A")
elif marks>70:
    print("b+")
elif marks>60:
    print("b")
elif marks>50:
    print("c+")
elif marks>40:
    print("c")
else:
    print("fail")