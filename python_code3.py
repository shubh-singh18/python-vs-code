# question 1 ->given a string use a for loop to count how  many vowels (a,i,e,o,u) it containas.

text=input("enter a  number")
count=0
for ch in text:
    if ch.lower() in "aieou":
        count=count+1
print(count)

# question 2 -> Write a program tp reverse a string using a for loop waithout using slicing 

text=input("enter a text")
rev=""
for i in range(len(text)-1,-1,-1):
    rev+=text[i]
print(rev)

# question 3->given a list of number use a for loop to find the largest numbers in the list.

lst=[23,54,67,87,56,95,83]
largest=lst[0]
for i in lst:
    if i>largest:
        largest=i
print(largest)


# question 4 ->2 se 10 tak ke tabele print karo 

for i in range(5,15):
    for j in range (1,11):
        print(i,"*",j,"=",i*j)

# question 5 -> ek list banano aur largest and smallest number find karo thik

lst=[45,67,89,33,55,24,78,865,57]
largest=lst[0]
smallest=lst[0]
for i in lst:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print(largest)
print(smallest)

# question 6->ek list bannao aur average find karo

lst=[45,65,67,86,79]
total=0
count=0
for i in lst:
    total+=i
    count+=1
average=total/count
print(average)