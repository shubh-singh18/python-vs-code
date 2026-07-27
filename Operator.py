# operator is a symbol used to perform operation such as addition,subtraction,comparison or logical operation on data.


# Arithmetic operator

a=int(input("enter a number"))
b=int(input("enter a number"))
print("addition of two value",a+b)
print("subtraction of two value",a-b)
print("multiplication ",a*b)
print("Modulus of two value",a%b)
print("Division of two value",a/b)
print("Exponentiation of two value",a**b)
print("Floor divsion of two value",a//b)


# comparison (Relational operators)

a=int(input("enter a first number"))
b=int(input("enter a second number"))
print("a>b",a)
print("a<b",b)
print("a>=b",a>b)
print("a<b",a<b)

#Logical opertors

a=-3
print(a>0 and a<10)
print(not(a>10))

#Assigment operators

x=10
x+=64
print(x)

#Bitwise operators

a=5
b=2
print(a&b)

#Ternary operator 

num=int(input("enter a number"))
result="positive" if num>0 else "negative"
print(result)

#special operators

a=[10,20]
b=a
c=[10,20]
print(a is b)
print(a is not ())



