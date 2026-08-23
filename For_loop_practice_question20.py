#find the largest number
#given a list of number use a for loop to find the largest number in the list.
number=[34,54,23,64,79,45,65,59,123,566,32434,56,3565,355764,354335,3455435433,4653555555]
largest=number[0]
for num in number:
    if num>largest:
        largest=num
        print(largest)