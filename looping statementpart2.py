
# question1-> find the sum off odd numbers.

a=int(input("enter a number"))
sum=0
for i in range (1,a+1):
    if i%2!=0:
     sum=sum+i
print(sum)

# question2-> find the sum of even numbers.

a=int(input("enter a nummber"))
sum=0
for i in range(1,a+1):
   if i%2==0:
       sum=sum+i
print("the sum of given even number",sum)


# question3-> given a string use a for loop to count how many vowels (a,i,e,o,u) it contains

text=input("enter a string")
count=0
for ch in text:
    if ch.lower() in ("a,i,o,u,e"):
        count+=1
print("count the vowels in letter",count)


# question4-> reverse a string
#write a program to reverse a string using a for loop without using slicing.

text=input("enter a letter")
reverse=" "
for i in range(len(text)-1,-1,-1):
   reverse+=text[i]
print(reverse)


#question5-> Find the largest number.
#Given a list of number,use a for loop to find the largest number in the list.

number=[21,32,43,55,76,86,34]
largest=number[0]
for num in number:
    if num>largest:
        largest=num
print(largest)

#question6->Fizz=bUzz
#print numbers from 1 to 100.for
#multiple of:
#3,print "fizz"
#5,print "Buzz"
#both 3 and 5 print "fizzbuzz" otherwise,print the number itself.

for i in range(1,26):
   if i%3==0 and i%5==0:
       print("Fizz Buzz")
   elif i%3==0:
       print("Fizz")
   elif i%5==0:
       print("Buzz")
   else:
       print(i)

#question6-> Muliplication table.
#Ask the user for a numbera and print its muliplication table up to 10.
#a=int(input("enter a number"))

for i in range(1,a+1):
    print("table of ",i)
    for j in range(1,11):
        print(i,"x",j,"=",j*i)
print()


#question7->
#*
#**
#***
#****
#*****
#print

rows=5
for i in range(1,rows+1):
    print("*"*i)