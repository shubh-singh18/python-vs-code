# Create an abstract class Animal with an abstract method sound(). Create Dog class and implement sound().
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("dog is barks")
aa=Dog()
aa.sound()
