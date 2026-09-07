a=int(input("enter a number"))
count=0
if (a>1):
    count=count+1
else:
    for i in range(1,a+1):
        if i%2==0:
            count=count+1
if count==0:
    print("prime")
else:
    print("not prime")
