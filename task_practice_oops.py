# 1. Student Class
# Create a Student class with:
# - college_name as class variable
# - name and marks as instance variables
# - display() as instance method
# - change_college() as class method
# - check_marks() as static method
# class student:
#     college_name="LIT college"

#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def display(self):
#         print(f"name{self.name},marks{self.marks}")

#     @classmethod
#     def a(cls,nn):
#         cls.college_name=nn
#         print(cls.college_name)

#     @staticmethod
#     def check_marks(nn):
#         if (nn>33):
#             print("pass")
#         else:
#             print("fail")

# a=student("devansh","90")
# student.a("aktu college")
# student.a(90)
# a.display()
# print(student.check_marks(90))


# Create an Employee class with:
# - company as class variable
# - name and salary as instance variables
# - display() as instance method
# - change_company() as class method
# - check_salary() as static method

class Employee:
    company_name="abc_company"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print(f"name{self.name},salary{self.salary}")

    @classmethod
    def a(cls,nn):
        cls.company_name=nn
        print(cls.company_name)

    @staticmethod
    def check_salary(salary):
        return salary>0

a=Employee("suraj","200000")
a.display()
Employee.a("xyz company")
print(Employee.check_salary(200000))
