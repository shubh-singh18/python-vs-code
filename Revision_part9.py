
# multiplication table
a=int(input("enter a number"))
for i in range(1,a+1):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

# print even number from 2 to 10
for i in range(2,11,2):
    print(i)


# find the largest and smallest number 
number=[23,43,56,86,354,87,45,776,56,66]
largest=number[0]
smallest=number[0]
for num in number:
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
print(largest)
print(smallest)

# list mein positive aur negative number count kare..

number=[34,-54,56,76,-88]
positive=0
negative=0
for num in number:
    if num>0:
        positive+=1
    if num<0:
        negative+=1
print(positive)
print(negative)

# list ka average calculate karo
number=[34,465,656,565,434]
total=0
count=0
for num in number:
    total+=num
    count+=1
average=total/count
print(average)

# list mein duplicated values find karo

number=[23,544,455,222,23,65,67]
for num in number:
    if number.count(num)>1:
        print(num)