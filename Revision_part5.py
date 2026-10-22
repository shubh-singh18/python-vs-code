
# find the sum of number

a=int(input("enter a number"))
sum=0
for i in range(1,a+1):
    sum=sum+i
print(sum)

# find the sum of even number

a=int(input("entrer a number"))
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

# given a string use a for loop to count how many vowels (a,i,e,o,u) it contains..

text=input("enter a number")
count=0
for ch in text:
    if ch.lower() in "aieou":
        count+=1
print(count)