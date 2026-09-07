class a:
    def d(self,marks):
        self.marks=marks
obj=a()
obj.d(180)
obj.marks=300
print(obj.marks)
 



class a:
    def add(self,marks):
        self.__marks=marks
        print(self.__marks)
obj=a()
obj.add(50)
obj.__marks=500
print(obj.__marks)





class a:
    def __init__(self,marks):
        self.__marks=marks

    def se(self):
        self.__marks=890

    def ge(self):
        print(self.__marks)

aa=a(45)
aa.se()
aa.ge()


class BaseEmployee:
    def show(self):
        pass
class Developer(BaseEmployee):
    def Calculate_salary(self,name,salary):
        self.salary=salary
        print(self.salary*(12/100))
class Manager(BaseEmployee):
    def Calculate_salary(self,name,salary):
        self.salary=salary
        print(self.salary*(15*100))
class Disiner(BaseEmployee):
    def Calculate_salary(self,name,salary):
        self.salary=salary
        print(self.salary*50/100)
obj=Developer("shivam",5000)
ob=Manager("Shubh",6000)
O=Disiner("Devansh",7000)





