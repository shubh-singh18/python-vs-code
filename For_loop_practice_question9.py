# List mein positive aur negative numbers count kare
number=[23,34,54,45,-45,-67]
positive=0
negative=0
for num in number:
    if num>0:
        positive+=1
    if num<0:
        negative+=1
print(positive)
print(negative)