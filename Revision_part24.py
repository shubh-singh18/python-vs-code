
# public access 
class student:
    def __init__(self):
        self.name="shubh"
a=student()
print(a.name)

# protected access modifiers


# protected access modifier
class student:
    def __init__(self):
        self.name="shubh"
class child(student):
    def display(self):
        print(self.name)
obj=child()
obj.display()

# private access modifier
class student:
    def __init__(self):
        self.__name="shubhsingh"

    def display(self):
        print(self.__name)
a=student()
a.display()


# getter and setter 
class student:
    def __init__(self):
        self.__marks=0

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        self.__marks=marks
a=student()
a.set_marks(90)
print(a.get_marks())
