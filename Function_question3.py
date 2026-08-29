# Largest Element in a List
# Write a function largest_element(numbers) that finds the largest element in a list without using the max() function.
def largest_element(number):
    largest=number[0]
    for num in number:
        if num>largest:
            largest=num
    return largest
number=(33,55,66,77)
print(largest_element(number))