
# question 1->1 se 100 tak number ko sum find karo 

sum=0
for i in range(1,101):
    sum=sum+i
print(sum)

# question 2-> 1 se 60 tak ke multiple of 5 print karo

for i in range(1,61):
    if i%5==0:
        print(i)

# question 3->list mein positive and negavtive number find karo

lst=[-34,45,65,-67,65,-56,90]
positvie=0
neagtive=0
for i in lst:
    if i>0:
        positvie+=1
    if i<0:
        neagtive+=1
print(positvie)
print(neagtive)

# question 4 ->list ka aaverage calculate karo

lst=[34,56,67,34,75,45]
total=0
count=0
for i in lst:
    total+=i
    count+=1
average=total/count
print(average)

# question5 -> list main duplicate value find karo

lst=[34,43,445,55,34,55]
for num in lst:
    if lst.count(num)>1:
        print(num)

# question 6>print table of 5

a=5
for i in range(1,11):
    print(a,"*",i,"=",a*i)