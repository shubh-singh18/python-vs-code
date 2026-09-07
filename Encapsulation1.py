#private access modifier

class student:
    def __init__(self):
        self.name="shubh"
aa=student()
print(aa.name)

#protected
class student:
    def __init__(self):
        self.name="shubh"
class child(student):
    def display(self):
        print(self.name)
obj=child()
obj.display()


#private
class student:
    def __init__(self):
        self.__name="shubh"

    def display(self):
        print(self.__name)
obj=student()
obj.display() 


