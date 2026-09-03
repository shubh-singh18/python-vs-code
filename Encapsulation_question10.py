# Create an Employee class with private __salary. Create methods to:
# set salary
# get salary
# increase salary by a given percentage

class Employee:
    def __init__(self,Employee):
        self.__salary=Employee

    def set_salary(self,salary):
        self.__salary=salary

    def get_salary(self):
        return self.__salary

    def increase_salary(self,percentage):
        increase=self.__salary*percentage/100
        self.__salary+=increase

e = Employee(30000)

print("Salary:", e.get_salary())

e.set_salary(35000)
print("Updated Salary:", e.get_salary())

e.increase_salary(10)
print("After 10% Increase:", e.get_salary())





