# Create a Employee class with a salary() method that calculates salary based on:
# basic salary only
# basic salary + bonus
# basic salary + bonus + allowance.

class Employee:
    def salary(self,basic_salary,bouns=0,allowance=0):
        total_salary=basic_salary+bouns+allowance
        print("total_salary",total_salary)
       

aa=Employee()
aa.salary(9000)
print()
aa.salary(9000,1500)
print()
aa.salary(9000,1500,2000)
print()
