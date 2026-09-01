# Create an Employee class with a salary() method. Create a Manager class that overrides salary() and displays the manager's salary.
class Employee:
    def salary(self):
        print("salary of employee is 50000")
class Manger(Employee):
    def salary(self):
        print("salary of manger is 1000000")
aa=Manger()
aa.salary()