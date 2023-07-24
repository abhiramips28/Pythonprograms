class Vehicle:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price
    def show(self):
        print('details',self.name,self.color,self.price)
    def max_speed(self):
        print("max speed is 150")
    def change_gear(self):
        print('Vehicle change 6 gear')

class Car(Vehicle):
    def max_speed(self):
        print("car max speed is 240")

    def change_gear(self):
        print('car change 7 gear')

car = Car("Ford",'grey',25000)
car.show()

vehicle = Vehicle("bmw",'black',30000)
vehicle.show()






