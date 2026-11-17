#question 1 find the factorail of the number:

a=5
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)

# question 2-> ek list lo uska factorail find karo

lst=[2,3,4,5,6,7,8]
for i in lst:
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    print(fact)


# question3 ->find the sum of number 

a=int(input("enter a number"))
sum=0
for i in range(1,a+1):
    sum=sum+i
print(sum)



# question4->find the sum of even numbers.

a=int(input("enter a number"))
sum=0
for i in range(1,a+1):
    if i%2==0:
        sum=sum+i
print(sum)

#question5 ->find the sum odd number:

a=int(input("enter a number"))
sum=0
for i in range(1,a+1):
    if i%2!=0:
        sum=sum+i
print(sum)

# question 6->print the prime number or not

a=int(input("enter a number"))
count=0
if (a<=1):
    count=count+1
else:
    for i in range(2,a):
        if a%i==0:
            count=count+1
if count==0:
    print("prime number")
else:
    print("not a primre")
