# Create an abstract class DataAnalysis with an abstract method analyze(). Create SalesAnalysis and CustomerAnalysis classes
from abc import ABC,abstractmethod
class DataAnalysis(ABC):
    @abstractmethod
    def analyze(self):
        pass
class SalesAnalysis(DataAnalysis):
    def analyze(self):
      print("salesanalysis is 50000")
class CustomerAnalysis(DataAnalysis):
    def analyze(self):

      print("customeranalysis is 400000")

aa=SalesAnalysis()
aa.analyze()
ab=CustomerAnalysis()
ab.analyze()
