class ppp:
    def __init__(self,marks):
        self.__marks=marks
    def ot(self):
        self.__marks=9000
        print(self.__marks)
ob=ppp(10)
ob.ot()
ob.__marks=560
print(ob.__marks)