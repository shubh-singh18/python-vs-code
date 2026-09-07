# Take a list of numbers containing duplicate values. Convert it into a set to remove duplicates and display the unique values.
number=(10,10,20,20,30,40,50,60)
for num in number:
 if number.count(num)>1:
  print(num)
  

