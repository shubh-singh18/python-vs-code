# Create a DataAnalyst class with an analyze() method. Create PythonAnalyst and ExcelAnalyst classes that override analyze() and
#  display how each analyst performs data analysis.
class DataAnalyst:
    def analyze(self):
        print("this is dataanalyst")
class PythonAnalyst(DataAnalyst):
    def analyze(self):
        print("this is pythonAnalyst")
class ExcelAnalyst(DataAnalyst):
    def analyze(self):
        print("this is ExcelAnalyst")

aa=ExcelAnalyst()
aa.analyze()
