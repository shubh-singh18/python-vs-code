# Create a Animal class with a sound() method. Create Dog and Cat classes that override the sound() method
class Animal:
    def sound(self):
        print("voice")
class dog(Animal):
    def sound(self):
        print("boof")
class cat(Animal):
    def sound(self):
        print("meow")

cat=cat()
dog=dog()
dog.sound()
cat.sound()
