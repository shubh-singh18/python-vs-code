#  list ka sum calculate karo
# number=(23,54,67,46)
# sum=0
# for i in number:
#     sum=sum+i
# print(sum)

# 1 se 100 tak number ka sum find karo:
# sum=0
# # for i in range(1,101):
# #     sum=sum+i
# # print(sum)


# numbers = (10, -5, 8, -2, 15,90,-91)

# positive = 0
# negative = 0

# for i in numbers:
#     if i > 0:
#         positive += 1
#     else:
#         negative += 1

# print("Positive:", positive)
# print("Negative:", negative)


# number=[34,54,66,76,45,49]
# largest=number[0]
# smallest=number[0]
# for num in number:
#     if num>largest:
#         largest=num
#     if num<smallest:
#         smallest=num
# print(largest)
# print(smallest)

# list=(23,22,10,45,46)
# for i in list:
#     if i%2==0:
#         print(i)

# number=(223,-45,4,-45,-54)
# posative=0
# negative=0
# for num in number:
#     if num>0:
#         posative+=1
#     if num<0:
#         negative+=1
# print(posative)
# print(negative)

# list=[34,105,156,67,72]
# total=0
# count=0
# for num in list:
#     total+=num
#     count+=1
# average=total/count
# print(average)

# list=(34,34,56,56,78,79,79,90,323,80,80)
# # for num in list:
# #     if list.count(num)>1:
# #         print(num)

# text=input("enter a number")
# reverse="" 
# for i in range(len(text)-1,-1,-1):
#     reverse+=text[i]
# print(reverse)

# number=(23,34,24,53)
# largest=number[0]
# second=number[0]
# for num in number:
#     if num>largest:
#         second=largest
#         largest=num
#     elif num>second and num!=largest:
#         second=num
# print(second)



# for i in range(1,51):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i)

# number=[23,445,34,34,54,55,21]
# largest=number[0]
# smallest=number[0]
# for num in number:
#     if num>largest:
#         largest=num
#     if num<smallest:
#         smallest=num
# print(largest)
# print(smallest)

# list=(23,22,45,44,67,68,90)
# for num in list:
#     if num%2==0:
#         print(num)

# number=(23,-43,34,-56,88,-90,88)
# positive=0
# negitive=0
# for num in number:
#     if num>0:
#         positive+=1
#     if num<0:
#         negitive+=1
# print("positive",positive)
# print("negitive",negitive)

# number=(34,56,107,153,72)
# total=0
# count=0
# for num in number:
#     total+=num
#     count+=1
# average=total/count
# print(average)

# number=(23,23,45,45,65,78,46,89,89)
# for num in number:
#     if number.count(num)>1:
#         print(num)

# text=input("enter a string")
# reverse="" 
# for i in range(len(text)-1,-1,-1):
#     reverse+=text[i]
# print(reverse)

# for i in range(1,54):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#             print(i)

# for i in range(1,51):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i)

# number=[23,43,43,41,11,19,10,20]
# for num in number:
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         print(num)

# number=[10,20,30,45,50]
# largest=number[0]
# second=number[0]
# for num in number:
#     if num>largest:
#         second=largest
#         largest=num
#     elif num>second and num!=second:
#         second=num
# print(second)

# def add():
#     a=20
#     b=30
#     print(a+b)
# add()
# add()

# Check Positive, Negative or Zero

def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(-5))

# def check_number(num):
#     if num>0:
#         return"positive"
#     elif num<0:
#         return"neagitve"
#     else:
#         return"zero"
# print(check_number(0))