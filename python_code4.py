# question 1 ->find the second largest number:

lst=[34,45,56,667,675,565,34464,56,900]
largest=lst[0]
second=lst[0]
for  i in lst:
    if i>largest:
        second=largest
        largest=i
    elif i>second:
        second=i
print(second)

# ek list ke saare number ko prime aur non prime ki list banano thik.

number=[2,3,4,5,6,7,8,9]
prime=[]
non_prime=[]
for num in number:
    if num<2:
        non_prime.append(num)
    else:
        count=0
        for i in range(1,num+1):
            if num%i==0:
                count+=1
        if count==2:
                prime.append(num)
        else:
                non_prime.append(num)
print("prime number",prime)
print("non prime number",non_prime)


# ek list ke saare number ka factorial find karo 

lst=[2,3,4,5,10]
for i in lst:
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    print(fact)

# find the prime numbers in a list

numbers=[2,11,5,17,6,18]
for num in numbers:
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num)


# 1 to 101 prime numbers find karo
#  
for num in range(1,101):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(num)






