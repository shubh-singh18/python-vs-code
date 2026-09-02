# Create an abstract class Employee with an abstract method salary(). Create Manager class and implement it.
from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass
class Manger(Employee):
    def salary(self):
        print("the salary is 500000")

aa=Manger()
aa.salary()
    