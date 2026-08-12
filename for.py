#print a table

a=int(input("enter a number"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)


#find the factorial of number

a=int(input("enter a number"))
fact=1;
for i in range(1,a+1):
    fact=fact*i
print(fact)

#find the sum of number
a=int(input("enter a number"))
sum=0;
for i in range(1,a+1):
    sum=sum+i;
print(sum)

#find the sum of even number
a=int(input("ente a number"))
sum=0;
for i in range(2,a+1,2):
    sum=sum+i;
print(sum)


#find the sum of odd nnumber
a=int(input("enter a number"))
sum=0;
for i in range(1,a+1):
    if i%2!=0:
        sum=sum+i
        print(sum)

#print the prime number or not 
a=int(input("enter a number"))
count=0
if(a<=1):
     count=count+1
     for i in range(2,a):
         if a%2==0:
             count=count+1
if count==0:
     print("prime number")
else:
    print("not a prime number") 

#given a string use a for loop to count how many vowels (a,i,e,o,u)

text=input("enter a text")
count=0
for ch in text:
    if ch.lower() in "aieou":
        count+=1
print(count)

# reverse a string
#write a program to reverse a string using a for loop wwithout using slicing .
text=input("enter a text")
reverse=" "
for i in range(len(text)-1,-1,-1):
    reverse+=text[i]
print(reverse)


try:
    with open("student.txt","r")as f:
        print(f.read())
except FileNotFoundError:
    print("error,file not fount")
finally:
    print("file operation completed")

