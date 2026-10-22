
# check three number greater number find

a=230
b=240
c=25
d=a if a>b else b if b>c else c
print(d)

# check four number greater number find

a=10
b=20
c=30
d=4
f=a if a>b else b if b>c else c if c>d else d
print(f)

# check person can vote or not 

age=2
print("vote" if age>18 else "not vote")


# check number is positive ,negative,zero

a=int(input("enter a number"))
print(a>0,"Positve")
print(a<0,"Negative" )
print(a==0,"Zero")


# check two number is greater number

a=int(input("enter a number"))
b=int(input("enter a number"))
if (a>b):
    print("a number is greater number")
elif (a<b):
    print("b is number is greater number")
else:
    print("both number are equall")

# leap year

year=int(input("enter a year"))
if (year%4==0 and year%100!=0)or (year%400==0):
    print("this is a leap year")
else:
    print("this is not a leap year ")

# vote 

a=int(input("enter a number"))
if (a>18):
    print("you can vote")
else:
    print("you can not a vote")

# triangle question 

side1=int(input("enter a side"))
side2=int(input("enter a side"))
side3=int(input("enter a side"))
if(side1+side2>side3)and(side1+side3>side2)and(side2+side3>side1):
    print("valid side")
else:
    print("invalid side")

# vowel question 

letter=(input("enter a letter"))
if letter in "aieou":
    print("vowel")
else:
    print("not a vowel")