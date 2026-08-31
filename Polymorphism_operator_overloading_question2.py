# Create a Student class and overload the > operator to compare the marks of two students.
class student:
    def __init__(self,marks):
        self.marks=marks
    def __gt__(self,other):
        return self.marks>other.marks
aa=student(89)
ab=student(70)
print(aa>ab)