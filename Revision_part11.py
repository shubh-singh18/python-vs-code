
# List in python
# List is a order and mutable connection of mutiple value.
# It can store multiple value
# it is order collection
# list is a mutable can be changed
# it allow duplicate value
# it can store differernt data type value
# change list item
fruits=["apple","banana","mango"]
fruits[1]="orange"
print(fruits)


# using append():Add item at the end
fruits=["apple","banana"]
fruits.append("mango")
print(fruits)

# using inserts ->add item at a specific position
fruits=["apple","mango"]
fruits.insert(1,"orange")
print(fruits)

# using items remove->remove a specific items
fruits=["apple","mango","banana"]
fruits.remove("apple")
print(fruits)

# using pop -> remove items by index (or last item)
fruits=["applle","banana","mango"]
fruits.pop()
print(fruits)
# using sort
a=[10,20,32,34,43,454,34]
a.sort()
print(a)

# reverse()
a=[21,23,32,35,76,45,87,35]
a.reverse()
print(a)

# count()
a=[23,54,67,46,97,35,35]
b=a.count(35)
print(b)

# index)()
a=[10,34,54,67,55,76,34,87,35,88]
print(a.index(67))