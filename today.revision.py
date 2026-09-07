# list
# list is a order or mutable collection and it can store duliple value and
#  store multiple value and it can possible slicing and it can store diffeerent data type
# list ko print kar diya hai 
# list=["shubh","shivam","devansh"]
# print(list)

# change the list:
# list=["shubh","shivam","devansh"]
# list[1]="prawajjal"
# print(list)

# list main method 
#1. using append add the item at the end
# a=[10,20,50]
# a.append(70)
# print(a)

# 2.using insert ye value ko add karta hai per specific postion per
# a=[20,30,40]
# a.insert(2,90)
# print(a)

# 3. using remove ye specific item ko remove karta hai
# a=[20,30,40,50,60]
# a.remove(40)
# print(a)

# 4.pop using pop method ye value ko specific postion per remove karta hai aur ye agar hmm index value nhi dete hai to ye last value ko remove karta hai
# a=[20,40,50,60]
# a.pop()
# print(a)

# 5. sort using method ye accessding order aur descrinding order main remove karta hai
# a=[20,40,14,67,23,100]
# a.sort()
# print(a)

# 6.reverse method ye list ko reverse karta hai
# a=[10,20,30,40,50]
# a.reverse()
# print(a)

# 7 count method ye batat hai ki specific element kitni baar prenet hai ye three valible main store kar na padtas hai 
# a=[23,45,45,67,45,45]
# b=a.count(45)
# print(b)

# 8 index() method ye batata hai ki kon sa element kis position per hai
# a=[23,45,65,45,46,75,77,56]
# b=a.index(75)
# print(b)

# # 9. clear( method) is remove all elemens
# a=[24,54,56,463,53,5]
# a.clear()
# print(a)

# 10.copy method is used to create a copy of a list.
# a=[23,40,3,50,670]
# ab=a.copy()
# print(a)
# print(ab)

# 11 extend() used to add multiple elements from another list
# a=[23,44,55,6,67,788]
# ab=[56,786,577]
# ab.extend(a)
# print(ab)

# # list ke function
# a=[20,30,40,5,60]
# print(min(a))
# print(max(a))
# print(len(a))
# print(list(reversed(a)))
# print(sorted(a))
# print(sum(a))

# Tuple 
# A tuple is order and immutable collection of iteam it can store mutiple value and it can contain 
# duplicate value it can posible indexing and slicing 
# it two bulid in method 
# count()
# index()
# count method is used to how many times a specified element appears in a tuple
# a=(23,40,60,70,40)
# b=a.count(40)
# # print(b)
# # index the index method is used to find the index (position) of the first of a specified element in a tuple 
# a=(34,54,67,46,75,5657)
# b=a.index(75)
# print(b)
# slicing
# a=(10,20,340,50)
# print(a[1:2])

# tuple ke function
# a=(20,30,8,50,60,70)
# print(min(a))
# print(max(a))
# print(sum(a))
# print(tuple(reversed(a)))
# print(sorted(a))

# set is unordered and store unique multiple value and duplicate value not store it is mutable 
# no indexing and slicing allow
# create a set
# a={10,20,30,40,50}
# print(a)

#empty set
# s=set()
# print(type(s))

# set ke method
# 1. add method item ko add karta hai bas
# a={10,20,30,40,50,60,70}
# a.add(110)
# print(a)

# # 2.update method is used to add mutiple value
# a={10,20,30}
# b={50,60,70}
# a.update(b)
# print(a)

# 3.remove() method is used to removd specific elemnts of a set
# a={20,40,50,80}
# a.remove(40)
# print(a)

# # 4. discard method yeremoved karta hai specific elements ko per agar element present nhi hai to error nhi deta hai
# a={20,40,50,60,70,2100}
# a.discard(20)
# print(a)

# 5.pop method ye ek elemnts ko remove karta hai bas
# a={10,320,45,65}
# a.pop()
# print(a)

# union method ye ye two or more set ko return karta hai ek hi set main
# a={10,20,30,40}
# b={50,60,70}
# c={110,200}
# print(a.union(b,c))

# intersection method ye common elements ko  find karta hai two or more set main
# a={10,20,30}
# b={20,30,40}

# print(a.intersection(b,))

#difference method ye find karta hai ki first set main elemts present ho aur second set main elemts present na ho 
# a={20,40,50}
# b={20}
# print(a.difference(b))

# symmetric _difference method
# # ye dono set ki value common na ho use nikla ta hai bas
# a={10,20,40}
# b={40,50}
# print(a.symmetric_difference(b))

# set ke function hai ye bas
# a={10,20,40,50}
# print(max(a))
# print(min(a))
# print(sum(a))
# print(sorted(a))
# print(len(a))


# dictionary in pytrhon
# dictionary is built-in data type in python that stores data in key-value pair aur key is  unique and it store dupilate value it is mutable and it is ordered
# creating a dictionary
# add a item
# student={
#     "name":"shubh",
#     "age":21,
    
# }
# student["sub"]="python"
# print(student)

# updating value value ko change kar deta hai
# student={
#     "name":"shubh",
#     "age":21
# }
# student["age"]=20
# print(student)

# # deleting item delete the specific items
# student={
#     "name":"shubh",
# #     "age":20
# }
# del student["name"]
# print(student)

# key is return all the key are present in dir
# student={
#     "name":"shubh",
#     "age":20
# }
# print(student.keys())

# get method
# get method is used to retrieve the value of a specified key from a dictionary .if the key does not exist it returnnone instead of rror
# student={
#     "name":"shubh",
#     "age":30,
#     "sub":"python"
# }
# print(student.get("city"))


# pop key-value ko remove kar deta hai
# student={
#     "name":"shubh",
#     "age":30
# }
# print(student.pop("age"))
# print(student)

# frozen set in Python
# #A frozen set is an immutable (unchanged)version of a set .once a fronzenset is created you caanot add,remove,or update its elemts
# number=([12,45,6,77])
# print(number)


# ternary operator
# a=200
# b=30
# ab="a is greater than b" if (a>b) else "b is greater than a"
# print(ab)

# find three number is greater
# a=2850
# b=678
# c=450
# ab="a is greater" if (a>b and a>c) else "b is grater number" if (b>a and b>c) else "c is greater number"
# print(ab)
# find four number is greater
# a=23999
# b=5699
# c=677
# d=89
# ab="a is greater number" if (a>b and a>c and a>d) else "b is greater number" if (b>c and b>d) else "c is greater number" if (c>d) else "d is greater number"
# print(ab)


