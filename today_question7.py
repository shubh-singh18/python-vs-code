# Write a function named factorial() that accepts a number and
#  calculates its factorial using a loop. Display the result for the given input.
def fac():
 a=5
 fact=1
 for i in range(1,a+1):
     fact=fact*i
 print(fact)
fac()