# Create a Student class with a method display() that displays:

# only name
# name and age
# name, age and course
# using default arguments.

class student:
    def display(self,name,age=None,course=None):
        print("name",name)

        if age:
            print("age",age)
        if course:
            print("course",course)

aa=student()

aa.display("devansh")
print()

aa.display("devansh",21)
print()

aa.display("devansh",21,"B.tech")
print()











