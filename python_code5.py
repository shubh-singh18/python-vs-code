# find the second largest nnumber in a list:

number=[34,656,66,3444,76,3544]
largest=number[0]
second=number[0]
for num in number:
    if num>largest:
        second=largest
        largest=num
    elif num<largest:
        second=num
print(second)

# string ko reverse kar do thikk

text=input("enter a number")
rev=""
for i in range(len(text)-1,-1,-1):
    rev+=text[i]
print(rev)

# fibonancci(n)


def fibonancci(m):
    a=0
    b=1
    for i in range(m):
        print(a)
        c=a+b
        a=b
        b=c
fibonancci(10)

# check karo ki prime numbers hai ki nhi

num=int(input("enter a number"))
count=0
if (num<2):
    count=count+1
else:
    for i in range(2,num):
        if num%i==0:
            count=count+1
if count==0:
    print("prime number hai yaar")
else:
    print("not prime hai yaar")