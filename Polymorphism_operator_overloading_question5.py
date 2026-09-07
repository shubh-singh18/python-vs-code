# Create a ComplexNumber class and overload the + operator to add two complex numbers.
class ComplexNumber:
    def __init__(self,complexnumber):
        self.complexnumber=complexnumber
    def __add__(self,other):
        return self.complexnumber+other.complexnumber

aa=ComplexNumber(5+2j)
ab=ComplexNumber(5-3j)
print(aa+ab)

class complexNumber:
    def __init__(self,complexnumber):
        self.complexnumber=complexnumber
    def __add__(self,other):
        return self.complexnumber+other.complexnumber
aa=complexNumber(5+6j)
ab=complexNumber(6-8j)
print(aa+ab)