
# use map with a lambda function to find the cube of every number a list
lst=[23,5,67,77,68,46]
print(lst)
var=list(map(lambda a:a*a*a,lst))
print(var)

# use filter with a lambda function to find all positive numbers from a list
lst=[33,45,-67,-7873]
print(lst)
var=list(filter(lambda a:a>0,lst))
print(var)

# use filter with a simple function to find all prime numbers from a list
def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
        return True 
lst=[3,4,5,6,7]
print(list(filter(is_prime,lst)))

# use filter  with a lambda a function to find all words whode length is greater than 5
lst=["ram","chauhan","shubhsingh"]
print(lst)
var=list(filter(lambda word:len(word)>5,lst))
print(var)



# use map with a simple function to convert temperture from calsius to fahrenhrit.
lst=[23,343,55,56,99]
print(lst)
def tempertaure(a):
    return (a*1.8)+32
var=list(map(tempertaure,lst))
print(var)


# use map with a lambda function to convert all integer into strings
lst=[23,34,65,676,86]
print(lst)
var=list(map(lambda a:str(a),lst))
print(var)


# file handling
with open("student101.txt","r")as f:
    a=f.read()
    print(a)

# tell()
f=open("student.txt","r")
print(f.tell())

# seek()
f=open("student101.txt","r")
print(f.seek(3))

# question1-> Safe Division Calculator
