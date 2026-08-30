#create a student class with name and marks of 3 subjects.create an object and calculate total and percentage.
class student:
    def __init__(self,name,hindi,maths,computer):
        self.name=name
        self.hindi=hindi
        self.maths=maths
        self.computer=computer
    def display(self):
        total=self.hindi+self.maths+self.computer
        percentage=total/3
        print("name",self.name)
        print("total",total)
        print("percentage",percentage)
aa=student("shubh",89,87,90)
aa.display()
