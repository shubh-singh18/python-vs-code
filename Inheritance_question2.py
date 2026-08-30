#create vehiicle class with a start() method.create a car class that inherits from vehicle.
class vehicle:
    def start(self):
        print("vehicle is starting")
class car(vehicle):
    pass
aa=car()
aa.start()
