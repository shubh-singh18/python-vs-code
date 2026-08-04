#question1=> write a function to check whether a number is even or odd.

def check(num):
    if num%2==0:
        return "even"
    else:
       return "odd"
number=int(input("enter a number"))
print(check(number))

#question2=> write a function to find the greatest of three numbers.

a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
def greatest(a,b,c):
    if a>b and a>c :
        return "a is greatest number"
    elif b>c:
        return "b is greatest number"
    else:
        return "c is greatest number"
print(greatest (a,b,c))


#question3=>wrtie a program to calculate the factorial of a number.

a=int(input("enter a number"))
def factorail (num):
 fact=1
 for i in range(1,1+num):
  fact=fact*i
 return fact
result=factorail(a)
print(result)

#question4=>write a function to check whether a string is a palindrome.

word=input("enter a string")
def palindrome (s):
    if s==s[::-1]:
        return True
    else:
        return False
if palindrome(word):
    print("palindrome")
else:
   print("not palindrome")

#question5=write a function to return the sum of average of a list

lst=[23,45,35,676,778,33]
def sum_average(num):
 total=sum(num)
 average=total/len(num)
 return total,average
total,average=sum_average(lst)
print(total)
print(average)



