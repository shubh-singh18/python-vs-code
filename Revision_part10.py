
# find the prime number in a list

number=[343,564,565,34,45,45,45,11]
count=0
for num in number:
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
         print(num)

# second largest number in a list

number=[34,45,67,56,34,87,23]
largest=number[0]
second=number[0]
for i in number:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
     second =i
print(second)


# Jump statements in python 
# in python jump statement are used to change the normal flow of execution in loops or function 
# the main jump statements are:
# break:
# The break statements immediatley terminates the loop.
for i in range (1,6):
    if i==4:
        break
    print(i)

# continue
# The continue statements skips the current itertiion and moves to the next itertion of the loop
for i in range(1,6): 
    if i==3:
        continue
    print(i)

pass
# the pass statements does nothing .it acts as a placeholder where code will be added letter 
for i in range(1,4):
    if i==2:
        pass
    print(i)