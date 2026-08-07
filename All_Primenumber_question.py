#check a number is prime or notprime number

a=int(input("enter a number"))
if a>1:
    for i in range(2,a):
        if(a%i==0):
            print(a,"is a not prime number")
            break
        else:
            print (a,"is a prime number")


#from 1 to 100 prime number
for num in range(1,101):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
               break
        else:
          print(num)


#from list of number prime number program

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for num in numbers:
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)   

#with recursion prime number program

number=int(input("enter  a number:"))
def is_prime_recursive(n,i=2):
    if n<=1:
        return False
    if i*i>n:
        return True
    if n%i==0:
        return False
    return is_prime_recursive(n,i+1)
if is_prime_recursive(number):
    print(number,"is a prime number")
else:
    print(number,"is a prime number")



#with lambda function prime number program

number=int(input("enter a number"))
is_prime=lambda x:all(x%i!=0 for i in range(2,int(x**0.5)+1))and x>1
if is_prime(number):
    print(number,"is a prime number")
else:
   print(number,"is not a prime number")



