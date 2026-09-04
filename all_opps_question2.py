
# 2. Employee Salary System — Inheritance + Polymorphism

# Create a base Employee class and three child classes:
# - Developer
# - Manager
# - Designer

# Requirements:
# - Each employee should have a name and base salary.
# - Create a calculate_salary() method.
# - Override calculate_salary() in each child class.
# - Each employee type should calculate the final salary differently

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def calculate_salary(self):
        pass

class Developer(Employee):
    def calculate_salary(self):
        return self.salary+(self.salary*12/100)

class Manger(Employee):
    def calculate_salary(self):
        return self.salary+(self.salary*18/100)

class Designer(Employee):
    def calculate_salary(self):
        return self.salary+(self.salary*25/100)

aa=Developer("prawjjal",50000)
print("developer",aa.calculate_salary())
ab=Manger("shubh",45000)
print("manger",ab.calculate_salary())
ac=Designer("shivam",40000)
print("designer",ac.calculate_salary())



















    