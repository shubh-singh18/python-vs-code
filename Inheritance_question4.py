#create a animal class with a sound() method.create a dog class that inherits from animals and overrides sound()
class Animal:
    def sound(self):
        print("Animals sound")
class Dog(Animal):
    def sound(self):
        print("dog sound is bow")
aa=Dog()
aa.sound()
