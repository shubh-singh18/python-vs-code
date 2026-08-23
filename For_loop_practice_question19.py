#reverse
#write a program to reverse a string using a for loop without using slicing .
text=input("enter a string")
reverse=""
for i in range(len(text)-1,-1,-1):
    reverse+=text[i]
print(reverse)