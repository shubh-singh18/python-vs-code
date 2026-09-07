# Create a class named Student with the attributes name, roll number, and marks. Create two objects 
# and display the details of both students using a class method.
class student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def display(self):
        print(self.name,self.roll_number,self.marks)
    def show(self):
        print(self.name,self.roll_number,self.marks)
obj=student("shubh",34,100)
obj.display()
obj.show()