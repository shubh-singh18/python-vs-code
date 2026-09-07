# Prime Number
# Write a function is_prime(n) that checks whether a given number
#  is prime or not. Return True if prime, otherwise False
def prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
        return True
a=int(input("enter a number"))
if prime(a):
    print("prime")
else:
    print("notprime")



# Factorial
# Write a function factorial(n) to calculate the 
# factorial of a number using a loop.
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("enter a number"))
print(factorial(n))

# Write a function largest_element(numbers) that
#  finds the largest element in a list without using the max() function.
def largest_element(number):
    largest=number[0]
    for num in number:
        if num>largest:
            largest=num
    return largest
number=(34,54,55,66,344,555)
print(largest_element(number))

# Second Largest Element
# Write a function second_largest(numbers) that finds the 
# second-largest distinct element without using sort() or max().
def second_largest(number):
    largest=number[0]
    second=number[0]
    for num in number:
        if num>largest:
            second=largest
            largest=num
        elif num>second and num!=largest:
            second=num
    return second
number=(67,55,78,88)
print(second_largest(number))

# Write a function count_vowels(text) that counts the number of vowels in a given string. The function should handle both uppercase and lowercase letters.
def count_vowels(text):
    count=0
    for ch in text:
        if ch.lower() in "aioue":
            count+=1
    return count
text=input("enter a letter")
print(count_vowels(text))


# Sum of Digits
# Write a function sum_of_digits(n) that returns the sum of 
# all digits of a number

# def sum_digits(n):
#     sum=0
#     for i in range(1,n+i):
#         sum=sum+i
#     return sum
# n=(3,5,6,5,4,5,6,6)
# print(sum_digits(n))

# Remove Duplicate Elements
# Write a function remove_duplicates(numbers) that removes duplicate
#  values from a list while maintaining the original order.


    
    
        






