# Create an abstract class Vehicle with an abstract method start(). Create Car class and implement start().
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("car is start with key")
aa=Car()
aa.start()