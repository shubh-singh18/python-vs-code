
# Write a function to count positive and negative numbers in a list.
def count(number):
    positive=0
    negative=0
    for num in number:
        if num<0:
            positive=positive+1
        elif num<0:
            negative=negative+1
    return positive,negative
number=(32,44,65,78,56)
positive,negative=(count(number))
print(positive)
print(negative)

# Write a function to calculate the sum of all elements in a list.
def smallest(number):
    smallest=number[0]
    for num in number:
        if num<smallest:
            smallest=num
    return smallest
number=(354,66,77,556,545,87)
print(smallest(number))


# use map with a simple function to find the square of every number in a list...
lst=[2,3,4,5,6,7,8]
print(lst)
def sqaure(a):
    return a*a
var=list(map(sqaure,lst))
print(var)

# use map with a lambda function to add 10 to every number in a list
lst=[34,544,67,34,33,67]
print(lst)
var=list(map(lambda a:a+10,lst))
print(var)

# use map with a lambda function to convert all names to uppercase
lst="shubhsingh"
print(lst)
var=list(map(lambda lst:lst.upper(),lst))
print(var)

# use filter with a simple function to find all even number from a list.
lst=[23,45,65,67,87,22,24,26]
print(lst)
var=list(filter(lambda a:a%2==0,lst))
print(var)

# use reducce with a lambda function to find the sum of all number in  a list
from functools import*
lst=[44,656,676,24]
print(lst)
var=int(reduce(lambda a,y:a+y,lst))
print(var)

# use reduce with a simple function to find the largest number in a list
from functools import*
lst=[12,34,45,65,778,898,644]
print(lst)
def largest(a,b):
    return a if a>b else b
var=int(reduce(largest,lst))
print(var)