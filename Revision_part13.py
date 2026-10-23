
# update() method
num={12,33,43,55}
num.update([100,200])
print(num)

# remove() method
num={10,20,30,40,50}
num.remove(40)
print(num)

# discard () method
num={10,20,30,40,50,60,70,80}
num.discard(50)
print(num)

# union method()
num1={10,20,30}
num2={30,40,60}
result=num1.union(num2)
print(result)


# intersection() method
set1={10,20,30,40,50}
set2={30,40,50,60,70}
result=set1.intersection(set2)
print(result)

# difference() method
set1={10,20,30,40,50}
set2={30,40,50,60,70}
result=set1.difference(set2)
print(result)

# symmetric_difference() method
set1={10,20,30,40,50,60,70}
set2={50,60,70}
result=set1.symmetric_difference(set2)
print(result)

# Dictionary in python
student={
    "name":"shubhsingh",
    "age":21,
    "marks":79
}
print(student)

# Accessing values
student={
    "name":"shubhsinghchauhan",
    "age":21
}
print(student["name"])
print(student["age"])

# Adding a new items.
student={
    "name":"shubhsinghchauhan"
}
student["course"]="python"
print(student)

# updating value
student={
    "name":"shubhsinghchauhan",
    "age":20
}
student["age"]=21
print(student)