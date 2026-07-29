# Loops are used to execute a block of code repeatedly until a condition is met  or all items in a squence processed.

# For Loop

# A for loop  is used to repeat a block of code a specific  number of time or to iterate over a collection of items.

#example 1

n=4
for i in range (0,n):
   print(i)


# question2-> Print numbers 1 to 5.

for i in range(1,6):
   print(i)


# question3-> print items in a list

fruits="apple","banana","orange"
for fruits in fruits:
   print(fruits)


#question4->print even numbers from 2 to 20

for i in range(2,21,2):
 print(i)


# question5-> print a list

name="shubhsinghchauhan"
for i in name:
   print(i)


 #question6->print a table

a=int(input("enter a numner"))
for i in range(1,11):
  print(a*i)


#question7->Find the factorial of number

a=int(input("enter a number"))
fact=1;
for i in range(1,a+1):
 fact=fact*i;
print(fact)


#question8->find the sum of number

a=int(input("enter a number"))
sum=0;
for i in range(1,a+1):
   sum=sum+i;
print(sum)


#question9->Find the sum of even number

a=int(input("enter a number"))
sum=0;
for i in range (1,a+1,2):
   sum=sum+i
   print(sum)


#question10->print the prime nummber or not.

a=int(input("enter a number"))
count=0;
if(a<=1):
    count=count+1
else:
   for i in range(2,a):
        if(a%2==0):
            count=count+1
if count==0:
 print("number is prime")
else:
 print("number is not a prime")


