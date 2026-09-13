# Q7. Create a variable x = 10, then assign "Python" to the same variable.
#  Print the value and its data type.
x="python"
x=10
print(type(x))

# Q8. Create:

# a = 25
# b = 10

# Print their sum, difference, multiplication and division.
a=20
b=30
print(a+b)
print(a-b)
print(a/b)
print(a*b)

# What will be the output?
x=10
print(x)
x="python"
print(x)

# print("hello","python","world")

print("hello",end=" ")
print("python")

print("A","B","C",sep="-")

# keyword
import keyword
print(keyword.kwlist)

# swap two number
a=10
b=20
a,b=b,a
print(a,b)

# swap two string
a="shubh"
b="singh"
a,b=b,a
print(a,b)

# swap two number with help of c
a=10
b=20
c=a
a=b
b=c
print(a,b)

# swap two number other method
a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)

# start and end
text="python"
print(text[0:2])

# slice from beginning
text="python"
print(text[:4])

# slice till end
text="python"
print(text[3:])

# copy entire string
text="python"
print(text[:])
# using set
text="python"
print(text[0:6:2])

# reverse a string
text="python"
print(text[::-1])

# negative index
text="python"
print(text[-4:-1])

# type casting
name="3445"
a=int(name)
print(type(a))

# impliciit casting
a=12
b=23.4
c=a+b
print(type(a+b))
# explicit casting
a=10.6
b=int(a)
print(type(b))

# Mutable
a=[12,34,54,66]
a.append(70)
print(a)

# immutable
text="python"
text="jython"
print(text)

# comparison (relational)operators
a=20
b=10
print(a==b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)

# logical oprators
a=5
print(a>0 and a<10)
print(not(a>10))

# Assigmment operators
x=10
x+=6
print(x)

# Bitwise operator
a=10
b=10
print(a&b)
#  Ternary operator 

num=10
result="positvie" if num>0 else "negative"
print(result)

# find the greatest numer of two
a=100
b=20
c=a if a>b else b
print(c)
# given three number and find the greatest number
a=1000
b=200
c=30
d="a" if a>b and a>c else "b" if b>c else "c"
print(d)
# given four number and find the greatest number

a=100000
b=2000
c=300
d=40
f="a" if a>b and a>c and a>d else "b" if b>c and b>d else "c" if c>d else "d"
print(f)


#write a program to calculate the sqaure and cube and sqaure of a number
a=int(input("enter a  number"))
sqaure=a**2
cube=a**3
print(sqaure)
print(cube)






