
# reverse a string

a=input("enter a number")
rev=""
for i in range(len(a)-1,-1,-1):
    rev+=a[i]
print(rev)

# find the largest nummber

number=[12,21,34,54,67,76,45,97,56]
largest=number[0]
for num in number:
    if num>largest:
        largest=num
print(largest)


# multiplication table..

a=int(input("enter a table"))
for i in range(1,a+1):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

# list main smallest number find karo... or largest number find karo...

number=[65,78,33,22,34,98]
largest=number[0]
smallest=number[0]
for i in number:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print(largest)
print(smallest)