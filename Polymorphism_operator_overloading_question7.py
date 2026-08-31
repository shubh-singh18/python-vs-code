# Fraction class banao aur + operator overload karke do fractions ko add karo.
# Example: 1/2 + 1/3 = 5/6

class Fraction:
    def __init__(self,num,den):
        self.num=num
        self.den=den
    def __add__(self,other):
        num=self.num+other.den+other.num+self.den
        den=self.den+other.den

        return Fraction(num,den)

aa=Fraction(3,4)
ab=Fraction(7,8)
res=aa+ab
print(res.num,"num","/",res.den,"den")