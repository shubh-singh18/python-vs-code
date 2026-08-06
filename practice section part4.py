#print number from 1 to 100.

for i in range(1,101):
 print(i)

#print number from 100 to 1

for i in range (100,0,-1):
 print(i)

#print the mulitplication table of a given number 

a=int(input("enter a table"))
for i in range(1,11):
    print(a,"*",i,"=",a*i)


#find the factorial of a number

a=int(input("enter a number"))
fact=1;
for i in range(1,a+1):
 fact=fact*i
 print(fact)

#check whether a  number is prime

a=int(input("enter a number"))
count=0
if (a<=1):
    count=count+1
for i in range(2,a):
    if(a%i==0):
        count=count+1
if count==0:
    print("number is prime")
else:
    print("number is not prime")    

#count vowels and consonants in a string.

text=input("enter a string")
count=0
for ch in text:
    if ch.lower() in "aieou":
        count+=1
print(count)


#print the fibonacci series up to n terms.

n=int(input("enter a number"))
a=0
b=1
for i in range(n):
    print(a,end="")
    c=a+b
    a=b
    b=c