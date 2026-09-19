# n numbers ke squares generate karne wala generator banao.
def squares ():
    n=[2,3,4,5,6,7,8]
    for i in n:
     yield i*i
x=squares()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


# Fibonacci series ke first n terms generate karne wala generator banao.
def fibonacci(n):
   a=0
   b=1
   for i in range(n):
      yield a
      a,b=b,a+b
x=fibonacci(11)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# decorator kya hai? decorator ek aise function hota hai jo kisi doores function ki functionality ko change ya increase karta hai bina
#  original function ka code change kiye
# question: Ek decorator banao jo function execute hone se pehle:
def a(x):
   def b():
     print ("Function start")
     x()
   return b
@a
def c():
   print("Hello")
c()



