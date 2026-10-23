
# Write a function to find the square of a number.
def square(num):
    return num*num
print(square(5))

# Write a function to check whether a number is even or odd.
def check_whether(num):
    if num%2==0:
        return "even number"
    else:
        return "odd number"
print(check_whether(23))


# Write a function to calculate the average of three numbers.
def average(a,b,c):
    return (a+b+c)/3
print(average(23,34,43))

# Write a function to find the largest of two numbers.
def largest(a,b):
    if a>b:
        return "a is a largest"
    else:
        return "b is a largest"
print(largest(45,65))


# Write a function to count the number of elements in a list.
def count_elemnts(number):
    count=0
    for num in number:
        count=count+1
    return count
number=(34,54,67,87,23,65,89)
print(count_elemnts(number))

def sum(number):
    sum=0
    for num in number:
        sum=sum+num
    return sum
number=(45,54,56,77,89,34)
print(sum(number))