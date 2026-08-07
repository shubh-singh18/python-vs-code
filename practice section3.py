#question1=>use a lambda function to find the sqare of a number

num=int(input("enter a number"))
var=(lambda a:a*a)(num)
print(var)

#quesstion2=>use a lambda function to find cube of a number

num=int(input("enter a number"))
var=(lambda a:a*a*a)(num)
print(var)


#question3=>sort a list of tuple based on the second element using a lambda function 
lst=[("shubh",21),("devansh",20),("shivam",9)]
print(lst)
var=sorted(lst,key=lambda x:x[1])
print(var)

#question4=>use map() to find the square of every number of list
lst=[2,4,5,6,12,34]
print(lst)
var=map(lambda a:a*a,lst)
print(list(var))

#question5=>use map() to convert a list of strings into uppercase

lst="shubh"
print(lst)
var=map(lambda a:a.upper(),lst)
print(list(var))

#question6=>use filter() to print only even numbers from a list
lst=[34,36,54,65,67,75,24,69]
print(lst)
var=filter(lambda a:a%2==0,lst)
print(list(var))

#question7=>use a filter() to print all prime numbers from a list

data=[2,3,5,7,11,34,54,19]
print(data)
var=list(filter(lambda n:n>1 and  all(n%i!=0 for i in range(2,n)),data))
print(var)


#question8=>use reduce() to find the sum of all elements in a list

from functools import*
lst=[24,43,54,105,56,67,32,23,23,11,7]
print(lst)
var=reduce(lambda a,b:a+b,lst)
print(var)


# find factorial using lambda function :

from functools import *
c=[10,3,4,6,8]
print(c)
fac=list(map(lambda x: reduce(lambda a,b:a*b,range(1,x+1)),c))
print(fac)


#print a list of table using lambda.

c=[12,32,43,7]
print(c)
var=map(lambda x:print(f"print the table of{x}")or[print(x,"x",i,"=",x*i)for i in range(1,11)],c)    
list(var)






