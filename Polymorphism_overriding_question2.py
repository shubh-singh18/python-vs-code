# Create a Vehicle class with a start() method. Create a Car class that overrides start() and prints "Car starts with key".
class Vehicle:
    def start(self):
        print("Vehicle is start")
class Car(Vehicle):
    def start(self):
        print("Car starts with key")
aa=Car()
aa.start()