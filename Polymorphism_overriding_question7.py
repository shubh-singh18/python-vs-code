# Create an Employee class with a work() method. Create a Developer class that overrides work() and prints "Developer writes code".
class Employee:
    def work(self):
        pass
class Developer(Employee):
    def work(self):
        print("developer writes code")

aa=Developer()
aa.work()
