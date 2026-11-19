# Find the missing number from a list.

lst=[1,2,3,5,6,7,8,9,10]
for i in range(1,11):
    if i not in lst:
        print(i)


# Reverse a list without using reverse() or slicing.

lst=[10,20,30,40,50]
new_lst=[]
for i in range(len(lst)-1,-1,-1):
    new_lst.append(lst[i])
print(new_lst)

# # Check whether a number is an Armstrong number or not.

num=152
total=0
digits=str(num)
power=len(digits)
for i in digits:
    total+=int(i)**power
if total== num:
    print("armstrong")
else:
    print("not armstrong")


# palindrome check
num=121
reverse=""
for i in str(num):
    reverse=i+reverse
if str(num)==reverse:
    print("palidrome")
else:
    print("not palindrome")


# palidrome check 
lst=[121,1331,123,441,576,565]
for num in lst:
 reverse=""
 for i in str(num):
  reverse=i+reverse
  if str(num)==reverse:
   print("palindrome")
  else:
   print("not palindrome")

