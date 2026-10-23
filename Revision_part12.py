
# clear()
a=[10,20,30,40,50,60,70,80,90]
a.clear()
print(a)

# copy()
a=[10,20,30,40,50]
b=a.copy()
print(a)
print(b)

# extend()
a=[10,20,40,30]
b=[50,60,70,80]
a.extend(b)
print(a)

tuple 
#   The count method is used to count how many times a specified elements appears in a tuple ..
number=(1,2,3,4,4,4,4)
print(number.count(4))

# index tuple
number=(23,43,45,65,677,45,65,67,665)
print(number.index(43))

max()
number=(33,54,676,87,23,88,121)
print(max(number))

len()
number=(454,46,67,232)
print(len(number))

sum()
number=(43,67,23,78,122)
print(sum(number))

sorted 
num=(30,10,20,54)
print(sorted(num))

set
# Add() method
num={12,23,34,45,56,67}
num.add(100)
print(num)