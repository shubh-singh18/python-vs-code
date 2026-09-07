# Create two sets of student names. Write a program to display the students who are common in both sets, students who are only in the first set,
#  and students who are only in the second set.
set1={"shubh","devansh","shivam"}
set2={"shubh","shivam","shiva"}
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))