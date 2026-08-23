# List mein duplicate values find karo
number=[23,45,67,76,78,98,45,67,98,109,76]

for num in number:
    if number.count(num)>1:
        print(num)

