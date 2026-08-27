# # Check Positive, Negative or Zero
def check_number(num):
    if num>0:
        return ("positve")
    elif num<0:
        return ("negitve")
    else:
        return ("zero")
print(check_number(0))

# Write a function to find the square of a number.
def square(num):
   return num*num
print(square(9))

# Write a function to check whether a number is even or odd.

def check_wether(num):
    if num%2==0:
        return "even number"
    else:
        return "odd number"
print(check_wether(55))

# Write a function to calculate the average of three numbers.
def average(a,b,c):
    return (a+b+c)/3
print (average(23,54,67))

# Write a function to find the largest of two numbers.
def largest(a,b):
    if a>b:
        return "a is largest"
    else:
        return "b is largest"
print (largest(2344,556))

# Write a function to count the number of elements in a list.
def count_elements(number):
    count=0
    for num in number:
        count=count+1
    return count
number=(34,54,56,34,34,34,23)
print(count_elements(number))

# Write a function to calculate the sum of all elements in a list.

def sum(number):
    sum=0
    for num in number:
        sum=sum+num
    return sum
number=(23,43,5,566)
print(sum(number))

# Write a function to count positive and negative numbers in a list.
def count(number):
    positive=0
    negative=0
    for num in number:
        if num>0:
            positive=positive+1
        elif num<0:
            negative=negative+1
    return positive,negative
number=(23,43,5,-35,-45,-65,-55)
positive,negative=(count(number))
print(positive)
print(negative)

# Write a function to find the smallest number in a list without using min().
def smallest(number):
    smallest=number[0]
    for num in number:
        if num<smallest:
            smallest=num
    return smallest
number=(23,43,55,76,8)
print(smallest(number))



 

                                           