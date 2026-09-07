# Create a tuple containing numbers. Write a program to find the largest and smallest values in the
#  tuple without using the built-in max() and min() functions.
a=[23,45,67,89,12]
largest=a[0]
smallest=a[0]
for num in a:
  if num>largest:
    largest=num
  
  elif num<largest:
    smallest=num
  else:
    print(smallest)
else:
  print(largest)


