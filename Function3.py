# write a function that accepts a list of number and return the sum, average ,largest number ,and smallest number.display all four results
# def alla(number):
#     total=0
#     largest=number[0]
#     smallest=number[0]
#     for num in number:
#         total=total+num
#         if num>largest:
#             largest=num
#         if num<smallest:
#             smallest=num
#     average=total/len(number)
#     return average,largest,smallest,total
# number=(45,65,66,41,6,66,77,88,68)
# print(alla(number))

#find the factorial in function 

# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# num=int(input("enter a number"))
# print(factorial(num))

#use map() with a simple function to find the square of every number in a list.
# lst=[34,4,5,6,78,12]
# print(lst)
# def square(a):
#     return a*a
# var=list(map(square,lst))
# print(var)

#use map() with a lambda function to add 10 to every number in a list
# lst=[45,66,45,33,23,43]
# print(lst)
# var=list(map(lambda a:a+10,lst))
# print(var)

#use map() with a lambda function to convert all names to uppercase.
# lst=["shubh","singh","chauhan"]
# print(lst)
# var=list(map(lambda lst:lst.upper(),lst))
# print(var)



def result(name, m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Name:", name)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)


name = input("Enter name: ")

m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))
m4 = int(input("Enter marks 4: "))
m5 = int(input("Enter marks 5: "))

result(name, m1, m2, m3, m4, m5)       

