# List in Python

#List is a order and mutable connection.
 #It can store multiple value
 #It allow duplicate value
 #It can store different data type value


# create a list 

a=["shivam","devansh","shiva","akash","20","True"]
print(a)
print(a[5])

#change list item

name=["shubh","devansh","suraj","shubham","harsh"]
name[2]="shiva"
print(name)

#List predefin function

#1.> Using append() :Add item at the end

name=["shubh","singh"]
name.append("chauhan")
#print(name)

#2.> using insert(): Add item at a specific position

num=[17,19]
num.insert(1,"18")
print(num)

#3.>using remove item ("remove()")

num=[12,13,14,20,15,16]
num.remove("20")
print(num)

#4.> using pop : Remove item by index(or last item).

num=[12,13,14,15,16,17]
num.pop()
print(num)

#5.>using sort() The sort method() is used to arrange the elements of a list in ascending or descending order

num=[23,43,12,5,13,9,34,41]
num.sort()
print(num)

#6.>reverse() : The reverse() method is used to reverse the order of elements in a list

num=[12,34,35,77,54]
num.reverse()
print(num)

#7.>count() : The count() method is used to count how many times a specific elements appears in a list

num=[34,10,34,78,28,34,76,34,34]
result=num.count("34")


#8.>Index() : Find the index of an item
#"The index() method is used to find the position(index)"

num=[34,54,66,56,65,45,35,564]
print(num.index(35))

#9.>Clear() : Remove all items

num=[34,54,655,44,33,65,656]
num.clear()
print(num)

#10.>copy() The copy() method is used to create a copy of a list

num=[12,32,44,54,67,87,89]
new_num=num.copy()
print(num)
print(new_num)

#11.>Extend :The extend () method is used to add multiple elements from another list.
num1=[23,56,7,897,67]
num2=[21,12,21,33,42,4]
num1.extend(num2)
print(num1)