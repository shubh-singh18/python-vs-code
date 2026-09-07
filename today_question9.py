# Write a Python program that accepts a list of numbers and finds the second largest number without using the sort() function.
a=(23,45,65,67)
largest=a
secondlargest=largest

for largest in a:
    if largest>secondlargest:
        secondlargest=largest
print(a)
