# Create an Animal class with a sound() method. Create a Dog class that overrides sound() and prints "Dog barks".
class Animal:
    def sound(self):
        print("the animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")
aa=Dog()
aa.sound()
