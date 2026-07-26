# string slicing means taking a part (substring) of a string using indexes.

#start and end
text="shubh"
print(text[0:2]) 

#slicing from begining
text="shubh"
print(text[:4])

#slicing till end
text="shubhsingh"
print(text[5:])

#copy entire string
text="shubhsinghchauhan"
print(text[:])

#using set
text="shubhsinghchauhan"
print(text[0:17:2])

#reverse a string
text="shubhsinghchauhan"
print(text[::-1])

#negative index
text="shubhsinghchauhan"
print(text[-7:-1])

 #question1
name="stringslicing"
print(name[0:6])
print(name[6:])
print(name[0:14:2])
print(name[::-1])
print(name[-7:])


#                  Type Casting
# we can convert one type two another type this conversion is called type casting

#example1
name="123"
a=int(name)
print(a)
print(type(a))


#example2

name="shubh"
a=bool(name)
print(a)
print(type(a))

#          type in type casting 
# 1> Implicit casting (Automatic type casting)
a=10
b=20
c=a+b
print(c)
print(type(c))

# 2> Explicit cassting(Manual type casting) 
a=23.5
b=bool(a)
print(b)
print(type(b))
