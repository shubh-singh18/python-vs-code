# Jump Statement in python

# Jump Statment are used to change the normal flow of exectution in loops or function.

#The main jump statement are:
# 1->Break
#2->Continue
#3->Pass

# Break

# The break statement immedialtly terminates the loop

#example 
for i in range(1,17):
    if i==15:
        break
    print(i)

#continue

#The continue statement is a skip the current iteration and move the next iteration.

#example
for i in range(12,45):
    if i==30:
        continue
    print(i)

#pass 
#The pass statement does nothing . It acts as a placeholder where code will be added later

#Example
for i in range(12):
    if i==6:
     pass
    print(i)