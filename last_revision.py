# break
# the break statement terminates the loop 
for i in range(1,7):
    if i==5:
        break
    print(i)

# continue
# the continues statement skips the current iteration and moves to the next iteration of the loop
for i in range(1,12):
    if i==6:
        continue
    print(i)

# pass 
# the pass statement does nothing .it acts as a placeholder where code will be added later :
for i in range(1,10):
    if i==2:
        pass
    print(i)


# list
# list is a order and mutable connection of multiple value 
# It can store multiple value
# It allow duplicate value
# It can store different data type value
# indexing and slicing are allow

a=[10,20,30,40,50]
a[1]=110
print(a)
# append(): Add item at the end
a=[10,20,30,40,50]
a.append(110)
print(a)
# using insert():ADDitems specific position
a=[10,20,30,40,50]
a.insert(1,120)
print(a)

# remove items: remove the item specific piostion
a=[10,20,30,40,50]
a.remove(20)
print(a)
# using pop : remove item by index (or last items)
a=[10,20,30,40,50,60]
a.pop()
print(a)

# using sort : the sort method is used to arrange the elements of a list in ascending (small to largest).
a=[23,43,455,33,64,567]
a.sort()
print(a)

# reverse() : the reverse the elemmts
a=[10,20,30,40,50]
a.reverse()
print(a)

# count : the count method is used to count how many times a specific elemnts appears in a list:
a=[10,20,30,10,10,20,10]
ab=a.count(10)
print(ab)

# index(): ye index batata hai spcific elements ki 
a=[10,20,30,40,50]
ab=a.index(30)
print(ab)

# clear(): removes all items:
a=[10,20,30,40,50]
ab=a.clear()
print(a)

# copy: the copy method is used to create a copy of a list
a=[10,20,30,40]
ab=a.copy()
print(a)
print(ab)

# extend : the extend method to add multiple elenmts from another list:
a=[10,20,30]
b=[40,50,60]
a.extend(b)

# Tuple
# a tuple in python is an ordered,immutable collectioon of items.once a tuple is created you cannot change its elements:
# suppport indexing and slicing

# slicing of tuple
a=(1,2,3,4,5,6)
print(a[1:5])

# count method is used to count how mmany times a specified elemments appears in a tuple
a=(10,20,30,40,50,30,30,30)
print(a.count(30))

# index method is used to find the index (position) of the first occurrence of a specified elements in w tuple .
a=(10,20,30,40,50)
print(a.index(50))

# function
a=(10,20,30,40,50,60,35)
print(max(a))
print(min(a))
print(sum(a))
print(len(a))
print(sorted(a))
b=tuple(reversed(a))
print(b)

# set is unordered and mutable it can store mutiple uniques and not store non-duplicates value .sets are unored and mutable
# Add method : the add method is add a single elemnts:
a={10,20,30,40}
a.add(70)
print(a)

# update : method is used to add mutiple elemnets to a set at once:
a={10,20,30,40}
b={50,60,70,76}
a.update(b)
print(a)

# remove :remove method is used to remove a specific elemnts from a set:
a={10,20,30,40}
a.remove(30)
print(a)

# discard method: method is used to remove a specific elemtns from a set . if the elenmts is not presents it does not raiser an error
a={10,20,30,40}
a.discard(70)
print(a)

# union method is combinetion of two or more set annd return a new sets:
a={10,20,30}
b={40,50,60}
d={110,220,330}
c=a.union(b,d)
print(c)

# intersection find the common elenments of two or more sets:
a={10,20,30}
b={10,50,60}
d={10,120}
c=a.intersection(b,d)
print(c)

# differnce() method:find the elemnts present in a first set but not present in second set 
a={10,20,340}
b={110,20}
c=a.difference(b)
print(c)

# symmetric_difference: is used to find elenmts that are present in either of the two sets but not in both it retuyrn a new set
a={10,20,30}
b={40,50,60}
c=a.symmetric_difference(b)
print(c)


# dictionay in python
# a dictionary is a bulit in data  type in python that stores data in key_value pairs . ecach key is uniqu and is used to access its corresponding 
student={
    "name":"shivam",
    "age":21
}
print(student)

student=dict(name='shubh',age=20)
print(student)

# Accessing values
student={
    "name":"shubh",
    "age":20
}
print(student["name"])
print(student["age"])

# Adding anew items
student={
    "name":"shubh",
    "age":21
}
student["course"]="py"
print(student)

# updating value
student={
    "name":"shubh",
    "age":20
}
student["age"]=12
print(student)

# delleting an items
student={
    "name":"shubh",
    "age":30
}
del student["age"]
print(student)

# keys
# the keys methods is used to return all the keys ppresent in a dictionary
student={
    "name":"shubh",
    "age":20,
    "course":"python"
}
print(student.keys())

student={
    "name":"shubh",
    "age":23,
    "course":"py"
}
print(student.keys())

# get() method is used to retrive the value of a specific key from a dictionary . 
# if the key does not exist it return none(or a defacults value if provided instead of raising an error)
student={
    "name":"shubh",
    "age":20
}
print(student.get("city"))


