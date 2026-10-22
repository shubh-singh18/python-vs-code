
# traffic light question

color=str(input("enter a string"))
if(color=="red"):
    print("stop")
elif (color=="yello"):
    print("slow down")
elif (color == "green"):
    print("go")
else:
    print("invalid")

# 
# for loop

for i in range(1,5):
    print(i)

# 
fruits=["Apple","Banana","Mango"]
for i in fruits:
    print(i)

# even number

for i in range(2,101,2):
    print(i)

# odd

for i in range(1,101,2):
    print(i)

# list

name="shubhsinghchauhan"
for i in name:
    print(i)

# table

a=int(input("enter a number"))
for i in range(1,11):
 print(a,"*",i,"=",a*i)


# factorial

a=int(input("enter a numbeer "))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)
