
# # Write a program to reverse a string using slicing.

a="shubhsingh"
print(a[::-1])


# Write a program to print every second character of a string using slicing

a="shubhsingh"
print(a[0:9:2])


# Write a program to print characters from index 2 to index 6 using slicing.

a="shubhsingh"
print(a[2:6])


# Write a program to check whether a string is a palindrome using slicing.

a="shubhsingh"
if a==a[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# # "PythonProgramming" me se sirf Python slicing se print karo.

a="pythonprogramming"
print(a[0:6])


# # "DataAnalytics" me se sirf Analytics slicing se print karo

a="dataanalytics"
print(a[4:13])

# # Write a program to print the string in reverse order with every second character skipped.

a="dataanalytics"
print(a[::-2])


# User se ek string input lo aur slicing ka use karke uski first half aur second half print karo.

text=input("enter a string")
mid=len(text)//2
print("first half",text[:mid])
print("second half",text[mid:])

# check two number greater number find

a=102
b=23
c=a if a>b else b
print(c)