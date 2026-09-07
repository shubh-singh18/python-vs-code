# # Method overloading
# class b:
#  def add(a,b):
#     print(a+b)
#  def add(a,b,c):
#     print(a+b+c)
# a=b()
# a.add(10,20,30)



class a:
    def __init__(self,marks):
        self.marks=marks
aa=a(50)
ab=a(100)
print(aa+ab)

class a:
    def __init__(self,marks):
        self.marks=marks
    def __truediv__(self,other):
        return self.marks/other.marks
aa=a(500)
ab=a(100)
print(aa/ab)


class a:
    def __init__(self,marks):
        self.marks=marks
    def __mul__(self,other):
        return a(self.marks*other.marks)
aa=a(50)
ab=a(100)
ac=a(200)
ad=a(300)
rev=aa*ab*ac*ad
print(rev.marks)




