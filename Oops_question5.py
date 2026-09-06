# 5. Create an Employee Payroll System.
#    Implement different employee types such as FullTimeEmployee, PartTimeEmployee,
#    and ContractEmployee.
#    Calculate salary differently for each employee type

class Employeepayrollsystem:
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employeepayrollsystem):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employeepayrollsystem):
    def __init__(self,name,hour,rate):
        self.name=name
        self.hour=hour
        self.rate=rate

    def calculate_salary(self):
        return self.rate*self.hour

class ContractEmployee(FullTimeEmployee):
    def __init__(self,name,contract):
        self.name=name
        self.contract=contract

    def calculate_salary(self):
        return self.contract

aa=FullTimeEmployee("Prawjjal",80000)
ab=PartTimeEmployee("shubh",90,800)
ac=ContractEmployee("shivam sir",50000)

print(aa.name,aa.calculate_salary())
print(ab.name,ab.calculate_salary())
print(ac.name,ac.calculate_salary())


# 5. Create an Employee Payroll System.
#    Implement different employee types such as FullTimeEmployee, PartTimeEmployee,
#    and ContractEmployee.
#    Calculate salary differently for each employee type

class Employeepayrollsystem:
    def Calculate_salary(self):
        pass
class FullTimeEmployee(Employeepayrollsystem):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def Calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employeepayrollsystem):
    def __init__(self,name,rate,hour):
        self.name=name
        self.rate=rate
        self.hour=hour

    def Calculate_salary(self):
        return self.hour*self.rate

class ContractEmployee(Employeepayrollsystem):
    def __init__(self,name,contract):
        self.name=name
        self.contract=contract

    def Calculate_salary(self):
        return self.contract

aa=FullTimeEmployee("prawjjal",80000)
ab=PartTimeEmployee("shubh",90,800)
ac=ContractEmployee("shivam sir",60000)

print(aa.name,aa.Calculate_salary())
print(ab.name,ab.Calculate_salary())
print(ac.name,ac.Calculate_salary())

        






