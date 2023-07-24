""" more than one child class is derived from a single parent class. """

class Vehicle:
    def info(self):
        print("This is vehicle")

class Car(Vehicle):
    def car_info(self,name):
        print("Car name is ",name)

class Truck(Vehicle):
    def truck_info(self,name):
        print("Truck name is :",name)

obj1 = Car()
obj1.car_info('BMW')
obj1.info()

obj2 = Truck()
obj2.info()
obj2.truck_info("FORD")