# Second Largest Element
# Write a function second_largest(numbers) that finds the second-largest distinct element without using sort() or max().
def second_largest(number):
    largest=number[0]
    second=number[0]
    for num in number:
        if num>largest:
            second=largest
            largest=num
        elif num>second and num!=second:
            second=num
    return second
number=(45,56,76,77,45,70)
print(second_largest(number))
