# Create an abstract class Report with an abstract method generate_report(). 
# Create SalesReport, CustomerReport and ProductReport classes and implement the method differently.
from abc import ABC,abstractmethod
class Report(ABC):
    @abstractmethod
    def generate_report(self):
        pass

class SalesReport(Report):
    def generate_report(self):
        print("salereport is generate")

class CustomerReport(Report):
    def generate_report(self):
        print("CustomerReport is generate")

class ProductReport(Report):
    def generate_report(self):
        print("productreport is generate")

aa=SalesReport()
aa.generate_report()

ab=CustomerReport()
ab.generate_report()

ac=ProductReport()
ac.generate_report()