# Write a program to print the first 5 characters of a string using slicing.
text="chauhan"
print(text[0:5])

# Write a program to print the last 4 characters of a string using slicing
text="chauhan"
print(text[-4:])

# Write a program to reverse a string using slicing.
text="chauhan"
print(text[::-1])

# Write a program to print every second character of a string using slicing
text="chauhan"
print(text[0:7:2])

# Write a program to print characters from index 2 to index 6 using slicing.
text="chauhan"
print(text[2:6])

# Write a program to check whether a string is a palindrome using slicing.
text=input("enter a string")

if text==text[::-1]:
    print("palindramoe")
else:
    print("not palindrome")

# "PythonProgramming" me se sirf Python slicing se print karo.
text="pythonprogramming"
print(text[0:6])

# "DataAnalytics" me se sirf Analytics slicing se print karo.
text="dataanalytics"
print(text[4:13])

# Write a program to print the string in reverse order with every second character skipped.
text="python"
print(text[::-2])


# User se ek string input lo aur slicing ka use karke uski first half aur second half print karo.

text=input("enter a string")
mid=len(text)//2
print("First half",text[:mid])
print('second half',text[mid:])

