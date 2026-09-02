# Create an abstract class Employee with name, salary and abstract method calculate_bonus().
#  Create Manager and Developer classes with different bonus calculations.
from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @abstractmethod
    def Calculate_bonus(self):
        pass

class Manager(Employee):
    def Calculate_bonus(self):
        bonus=self.salary*10/100
        print("manger bonus",bonus)

class Developer(Employee):
    def Calculate_bonus(self):
        bonus=self.salary*15/100
        print("Developer bonus",bonus)

aa=Manager("prawjjal",50000)
aa.Calculate_bonus()
ab=Developer("shubh",45000)
ab.Calculate_bonus()


