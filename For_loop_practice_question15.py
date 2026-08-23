#find the sum of even number
a=int(input("enter a number"))
sum=0;
for i in range(2,a+1,2):
    sum=sum+i;
print(sum)