#question1=> create a tuple and print all elements

number=(12,34,56,78,978)
print(number)

#question2=>count the occurrence of an elements in a tuple

number=(23,43,56,43,34,43,34,23,89,677,43)
print(number.count(43))

#question3=>find the index of the elements in a tuple

number=(23,43,55,34,23,76,89,67,)
print(number.index(89))

#question4=>convert a tuple into a list and add a new element.

number=(12,33,45,67,8,68,89)
number=list(number)
number.append(100)
print(number)

#question5=>Find the maximum and minimum values in a tuple
 
number=(12,34,56,86,78,98,45)
print(number,max(number))
print(number,min(number))

#question6->create a set and print all elements.

number={12,34,54,67,87,90}
print(number)

#question7->Find the union of two sets.

a={23,54,56,7,67,89,90}
b={12,32,43,52,54,67,90}
print(set(a).union(set(b)))

#question8->find the intersection of two sets

a={12,23,45,67,89,56,765}
b={12,45,34,65,77,89}
print(set(a).intersection(set(b)))

#question9=>find the difference between two set

a={12,43,45,66,77,57,6,78,66}
b={12,43,77,534,676,88,88,66}
print(set(a).difference(set(b)))

#question10=>Remove duplicate values from a list using a set

a={12,23,23,45,34,45,67,67,89,56,56,90,100,100}
print(set(a))