# oops ?
# Object - Oriented Programming System
# ye ek approch hai jjisme hm log program ko class object ke arround bantai-hai

# Class?
# Class is a blueprint for creating object
class student:
    nam="shubhsing"


# Object
# A Object is a real world entity an contain its own state and behavior defined by a class.
s1=student()
print(s1.name)

#Example 1
class car:
    color="red"
    brand="mercedes"
car1=car()
print(car1.color)
print(car1.brand)

# constructor ye __init__function
# jise hi hmm kise class ke object banate hai vaise  hi __init__ method executed ho jata hai. 

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("shubh",21)
print(s1.name,s1.age)

# self?
# self current object ko refers kat ta hai.

class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
        print("adding new student data in database")
s1=student("shiva",23,88)
print(s1.name,s1.age,s1.marks)
s2=student("suraj",26,98)
print(s2.name,s2.age,s2.marks) 

# Attributes
# variable defines inside the class are attributes

# Method
# Function defines inside the class are method

# Example
class Animal:
    species="Dog"  # Attributes
    def make_sound(self): # method
        print("Bark")

# type of attributes
# class attributes
# A normal variable created  inslide a class is called class varible

#Instance attributes
# A variable created using instance like self.name, self.age, self.marks

# Example
class car:
 wheels=4 # class attributes
def __init__(self,color):
 self.color=color #instance attribute

# types of methods
# Instance methods
# A instance method work with instance(object) of class.

# Example2
class student:
   college_name="Lit college"
   def __init__(self,name,age,marks):
      self.name=name
      self.age=age
      self.marks=marks

   def show(self):
      print("hello",self.name,self.age,self.marks,student.college_name)
s1=student("shiva",23,78)
s1.show()