""" Combination of different inheritance called hybrid inheritance."""

class Vehicle:
    def info(self):
        print("This is vehicle")

class Car(Vehicle):
    def car_info(self,name):
        print("Car name is ",name)

class Truck(Vehicle):
    def truck_info(self,name):
        print("Truck name is :",name)

class Sportscar(Car,Vehicle):
    def sports_car_info(self):
        print("Inside the sports car class")

obj1 = Car()
obj1.car_info('BMW')
obj1.info()

obj2 = Truck()
obj2.info()
obj2.truck_info("FORD")

obj3 = Sportscar()
obj3.car_info('BMW')
obj3.info()
obj3.sports_car_info()