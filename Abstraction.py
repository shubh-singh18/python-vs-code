from abc import ABC,abstractmethod
class a(ABC):
    @abstractmethod
    def sound(self):
        pass
class b(a):
    def sound(self):
        print("the dog is barking")
obj=b()
obj.sound()



from abc import ABC,abstractmethod
class Animal(ABC):
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks")
a=Dog()
a.sound()