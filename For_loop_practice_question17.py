# Print the prime nummber or not.
a=int(input("enter a  number"))
count=0
if a<=1:
    count=count+1
else:
    for i in range(2,a):
        if a%i==0:
            count=count+1
if count==0:
    print("prime number")
else:
    print("not prime number")