# Tuple in python
# A Tuple in python is an ordered,immutable collection of items.once a tuple is created, you cannot change its element
#characteristics of tuple
#Elements are stored in a fixed order.
#After creating a tuple, you cannot add, remove,or modify,its elements.
#A tuple can contain duplicate elements
#can store different data types
#you can access elements using indexes and slices


# creating tuple

a=("shubh","devansh","shivam","ram");
print(a)
print(type(a)) 

#Slicing of tuple

numbers=(10,20,30,40,50)
print(numbers[1:4])

#Count of tuple
#The  count() method is used to count how many times a specified elements appears in a tuple.

numbers=(2,3,4,2,2,3,2,5,6,7,2)
print(numbers.count(2))

#Index of tuple
#The index () method is used to find the index(position)of the first occurrence of a specified element in a tuple 

name=("shubh","singh","chauhan")
print(name.index("chauhan"))

#Max()Function in python
#The max() function is used to find the largest (maximum)elements in a tuple (or other iterable such as a list or string.)

num=(10,20,30,40,50,60)
print(max(num))

#min()function in python
#This min()function is used to find the smallest(minimum) elements in a tuple or other iterable like a list or string

num=(23,43,45,23,56,66)
print(min(num))


#Tuple function

#Len()function
#used to find the number of elements in a tuple

a=(10,23,45,65,67)
print(len(a))

#sum()function
#used to find the sum of all numeric elements in a tuple

a=(23,43,54,34)
print(sum(a))


#sorted()function
#used to sort the elements of a tuple.It returns a list,not a tuple

a=(23,33,32,12,16,56,43,78,53)
print(sorted(a))