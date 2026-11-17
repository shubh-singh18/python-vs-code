#question 1->  list ke saare number print karo

lst=[3,5,6,7,8,10]
for i in lst:
    print(i)

# question2-> list ka sum calculate karo 

lst=[50,50,40,60]
sum=0
for i in lst:
    sum=sum+i
    print(sum)


# question3 ->list mein maximum number find karo

lst=[56,98,35,97,444]
maximum=lst[0]
for i in lst:
    if i>maximum:
        maximum=i
print(maximum)


# question4 ->list mein minimum number find karo

lst=[56,68,87,90,21]
minimum=lst[0]
for i in lst:
    if i<minimum:
        minimum=i
print(minimum)


# question5 -> list mein even number count karo

lst=[3,4,12,32,545,56,67]
for i in lst:
    if i%2==0:
        print(i)
    

# question 5 list mein odd number count karo

lst=[32,45,67,98,99,44,22,11]
for i in lst:
    if i%2!=0:
        print(i)

