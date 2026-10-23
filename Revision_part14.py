
# deleting an items
student={
    "name":"shubhsinghchauhan",
    "age":21
}
del student["age"]
print(student)

# keys
# the keys method is used to return all the keys pressent in a dictionary
student={
    "name":"shubh",
    "age":20,
    "course":"python"
}
print(student.keys())



# get() method in python dictionary
student={
    "name":"shubhsinghchauhan",
    "age":21,
    "course":"python"
}
print(student.get("name"))

# frozen set in python
number=frozenset([1,2,3,4,5,6])
print(number)

# calling
# calling means when we want function we call it for use:
# Parameter is a variable used in a function to receive.
# Arguments->They are the value for while calling..
# return statements->function take values from paramenter annd make logic return the value.

# check number is even or odd
def even(num):
    if num%2==0:
        return ("even number")
    else:
        return ("odd number")
dev=even(21)
print(dev)

 # Check Positive, Negative or Zero
def check_number(num):
    if num>0:
        return  ("positive")
    elif num<0:
        return ("negative")
    else:
        return ("zero")
print(check_number(-21))
