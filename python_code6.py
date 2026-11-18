#  find the common elements between two lists

lst1=[12,23,34,45]
lst2=[12,23,90,67]
common=[]
for i in lst1:
    if i in lst2:
        common.append(i)
print(common)


# find eleemtns that are present in the first list but not in the second list

lst1=[10,20,30,40,50]
lst2=[10,40,100,200,300]
not_second=[]
for i in lst1:
    if i not in lst2:
        not_second.append(i)
print(not_second)


# Move all zeros to the end of a list.

lst=[3,5,0,3,0,5,0,20]
zero=[]
non_zero=[]
for i in lst:
    if i==0:
        zero.append(i)
    else:
        non_zero.append(i)
result=non_zero+zero
print(result)




# Separate positive and negative numbers into two different lists.

lst=[34,45,-67,-42]
positive=[]
negative=[]
for i in lst:
    if i>0:
        positive.append(i)
    else:
        negative.append(i)
print(positive)
print(negative)

# Find the frequency of every element in a list.

lst=[34,67,89,78,78,90]
for i in lst:
    count=0
    for j in lst:
        if i==j:
            count+=1
    print(i,":",count)
