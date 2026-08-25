# #list ke saare number print karo.
list=(2,3,4,5,6,7)
for i in list:
     print(i)

#list ka sum calculate karo.
a=(2,3,4,5,6,7,8)
sum=0
for i in a:
    sum=sum+i
print(sum)

# #list main maximum number find karo
number=(23,43,56,76,78)
largest=number[0]
for num in number:
    num>largest
    largest=num
print(largest)

# #list mein minimumm number find karo
number=(23,54,56,34,76,86,23)
largest=number[0]
for num in number:
    largest>num
    num=largest
print(largest)

# #list main odd number print karo.
number=(23,22,45,44,66,78,90,77)
for num in number:
    if num%2!=0:
        print(num)

# 1 to 100 tak ke number ka sum print karo.

sum=0
for i in range(1,101):
    sum=sum+i
print(sum)

# # 1 to 50 tak ke multiple of 5 print karo.
for i in range(1,51):
   if i%5==0:
      print(i)

#print the table of 5:
a=4
for i in range(1,11):
    print(a,"*",i,"=",a*i)

# #find the factorial of the number.
a=int(input("enter a number"))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)


#find the sum of number
a=int(input("enter a number"))
sum=0
for i in range(1,a+1):
    sum=sum+i
print(sum)

#find the sum of even number:
a=int(input("enter a number"))
sum=0
for i in range(1,a+1):
    if i%2==0:
         sum=sum+i
print(sum)

# find the sum of odd number:
a=int(input("enter a number"))
sum=0
for i in range(1,a+1):
    if i%2!=0:
        sum=sum+i
print(sum)

#find the prime or not
a=int(input("enter a number"))
count=0
if (a<=1):
    count=count+1
else:
    for i in range(1,a+1):
        if a%2==0:
            count=count+1
if count==0:
    print("prime number")
else:
    print("not prime")

# #given a string use a for loop to count how many vowels (a,i,e,o,u) it contain.
text=input("enter a text")
count=0
for ch in text:
    if ch.lower() in "a,i,e,o,u":
        count=count+1
print(count)

# # write a program to reverse string using a for loop without  using slicing:
text=input("enter a string")
reverse="" 
for i in range(len(text)-1,-1,-1):
    reverse+=text[i]
print(reverse)

#given a list of number use a for  loop to find the largest number in the loop. 
number=(23,43,56,78,45)
largest=number[0]
for num in number:
    if num>largest:
        largest=num
print(largest)

# Fizz Buzz
# print numbers from 1 to 100 .for muliple to 3 print "fizz"
# 5 print "bizz"
# both 3 and 5 print "fizzbuzz", otherwise the num itself
for num in range(1,1001):
    if num%3==0 and num%5==0:
        print("FizzBizz")
    elif num%5==0:
        print("Bizz")
    elif num%3==0:
        print("Fizz")
    else:
        (num)

# #create a list print the table
number=(2,3,4,5,6,7)
for num in number:
    for i in range(1,11):
        print(num,"*",i,"=",num*i)

# # print a table 1 to 10
for i in range(1,16):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

# user se input le kar table print karo

a=int(input("enter a number"))
for i in range(1,11):
    print(a,"*",i,"=",i*a)




