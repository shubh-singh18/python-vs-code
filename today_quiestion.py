# print(1)
# print(2)
# print(3)
# print(4)

# it is use the we want to iterate over sequence or repeat something known number of time 
# sytax of for loop:

# for variable name in squence:
#     statement
#  for l in range(2,101,2):
#     print(l)

# a=[10,20,30,40]
# for l in a:
#     print(l)

# a=[2,3,4,5,6]
# for i in a:
#     if i%2==0:
#         print("even")
#     else:
#         print("even")

# a=int(input("enter a number"))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

# a=int(input("enter a number"))
# count=0
# if(a<=1):
#     count=count+1
# else:
#     for i in range(2,a):
#         if (a%i==0):
#             count=count+1
# if count==0:
#     print("prime")
# else:
#     print("not prime")

a=101
sum=0
for i in range(2,a+1,2):
    sum=sum+i
print(sum)