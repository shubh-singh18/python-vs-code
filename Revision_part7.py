
# list mein positive aur negative number count kare..

number=[33,5,-57,87,23,-87,56,-34]
positive=0
negative=0
for num in number:
    if num>0:
        positive+=1
    if num<0:
        negative+=1
print(positive)
print(negative)

# list ka average calculate karo...

number=[45,56,78,89,12,43]
total=0
count=0
for num in number:
    total+=num
    count+=1
average=total/count
print(average)

# list mein duplicate values find karo...

number=[23,32,23,56,7788,778,667]
for num in number:
    if number.count(num)>1:
        print(num)

# find the prime number in a list 

number=[21,23,11,55,6644,77,45]
for num in number:
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num)

# 1 to 101 prime number find karo 

for num in range(1,101):
    count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
    if count==2:
        print(num)

# second largest number in a list

number=[23,34,45,5,64,33,3432]
largest=number[0]
second=number[0]
for i in number:
    if i>number:
        second=largest
    elif i>second and i!=largest:
        second=i
print(second)
